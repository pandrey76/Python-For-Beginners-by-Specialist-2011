#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 12.03.2012

@author: Prapor
'''
import sqlite3
import os.path

import mDocuments
import mNakPos

 
def create ():
    '''Create new Document'''
    return Nakladnay(status = mDocuments.Document.New)

#------------------------------------------------------------------------#     
class Nakladnay( mDocuments.Document ):
    '''
    classdocs
    '''
#Можно записать так
#    def __init__ ( self, id = None, **kwargs )
#        mDocuments.Document.__init__(self, id, **kwargs)
    def __init__(self, **kwargs ):
        '''
        Constructor
        '''
        mDocuments.Document.__init__(self, **kwargs)

        #TODO: Первый подход инициализации переменной
        #--------------------------------------------
        #if "itogo" in kwargs :
        #    self.__Itogo = kwargs["itogo"]
        #else :
        #    self.__Itogo = None
        #--------------------------------------------    
        #Можно и так записать
        self.__Itogo = kwargs["itogo"] if "itogo" in kwargs else None
        self.__Positions = []
        
#
    itogo = property( lambda self : self.__Itogo)
    
        #TODO: Второй подход инициализации переменной
        #      т.е. если переменная вообще может быть
        #      не определена. Данный подход считается 
        #      более Python-овским.
        #--------------------------------------------

    @property
    def _itogo(self):
        try :
            return self.itogo
        except AttributeError :
            return None
        #--------------------------------------------

#Из класса делаем генератор функцию
    def __iter__(self):
        for P in self.__Positions :
            yield P
            
#Пререопределяем метод __len__
    def __len__(self):
        return  len(self.__Positions)   
#Можно записать и так
#    __len__ = lambda self:  len(self.__Positions)
    
#    def get_position( self, index ):
#метод get_item заставляет экземпляр нашего класса вести
#себя подобно словарю, а не списку, но в данной ситуации он ведёт себя как список
    def __getitem__( self, index ):
        return self.__Positions[index]
    
    def append_blank( self, **kwarg ) :
        #TODO: 1. Функция должна принемать параметры соответствующие
        #TODO:    параметрам конструктора класса NakPos
        #TODO:    и добавлять в накладную позицию с этими параметрами.
        self.__Positions.append( mNakPos.NakPosition( **kwarg) )
        
    def append( self, position ):
        #Проверяем тип параметра
        if isinstance( position, mNakPos.NakPosition) :
            raise ValueError
        self.__Positions.append( position )
    
    def delete( self, index ):
        del self.__Positions[index] 

    def save(self):
        with self.connect( ) as conn :
            self._save(conn)
            curr = conn.cursor()
            curr.execute(
                """
                    update t_document
                        set f_kind = ?
                        where i_id = ?
                """, ( 1, self.identificator)
                #Константы в SQLных скриптах стараются не писать,
                #хотя это и не является ошибкой,
                #указывают непосредственно значение. 
                         )
            
            #При попытке выполнения последующей команды если создаём новую 
            #накладную, то всё будет в порядке, если накладная с таким
            #r_id_document уже есть, то будет выдано исключение  
            try :
                curr.execute(
                        """
                        -- r_id_document - поле не autoincrementno но prinary key
                        insert into t_nakladnay ( r_id_document, f_itogo )
                            values ( ?, ? )
                        """, ( self.identificator, self._itogo  )
                         )
            except sqlite3.IntegrityError :
                #Если у на с строчки с таким id нет, то команда update 
                #пройдёт без следно ( без ошибок, т.е. ничего не сделает )
                #В большенстве SQL существует возможность узнать сколько строк
                #было затронуто командой, но в SQLite такой возможности нет.
                #Поэтому мы пробуем вставить, если такой id есть, то мы пробуем обновить
                curr.execute(
                """
                    update t_nakladnay
                        set f_itogo = ?
                        where r_id_document = ?
                """, ( self.itogo, self.identificator )
                )
            # TODO: Здесь записать позиции по накладной
            
            
    def restore (self):
                # TODO: 1. Проверить неизменность типа документа
        with self.connect( ) as conn :
            curr = conn.cursor()
            
            curr.execute(
                """
                    select doc.f_status, nak.f_itogo
                    from t_document doc
                    inner join t_nakladnay nak
                        on doc.i_id - nak.r_id_document
                    where i_id = ?
                """, ( self.identificator, )                
                )
            #Здесь мы получаем данные по идентификатору
            #Если данных нет, то мы достигаем конца цикла и сразу переходим к блоку else
            #в котором генерируется исключение NotFound, если данные есть то мы их считываем и
            #по break минуем блок else
            for ( status, itogo ) in curr :
                #Нарушаем закрытость аттрибутов базового класса
                self._Document__Status = status
                if self._Document__Status == None :
                    del self._Document__Status
                
                self.__Itogo = itogo
                if self.__Itogo == None :
                    del self.__Itogo
                break
            #В Pythone цикл for или while, могут иметь команду else как условие if
            #else в цикде выполняется тогда и только тогда когда цикл завершается
            #по нарушению условия. Когда была выполнена проверка условия и условие оказалось нарушено
            #для цикла for else выполняется если мы достигаем конца цикла.
            #если мы выполняем команду break команда else не выполняется 
            else :
                raise mDocuments.NotFound()
           
            # TODO: Здесь считать позиции по накладной.  
                
    def __unicode__(self):
#    def |__str__(self):
#    def |__repr__(self):
#    def dump  (self):
        Posit = u""
        K = 1
#        for P in self.__Positions :
        for P in self : #мы переопределили метод __iter__ и из объекта сделлали генератор функцию 
            Posit += u"%d. %s\n" % ( K, unicode(P) )
            K += 1

        Result = u"(ID:%s) (Status:%s\n" % ( unicode(self._identificator),
                                             unicode(self._status) )
        Result += u"Накладная\n"
        Result += u"%s" % ( Posit, )
        Result += u"Итого %s" % ( self._itogo) 

#Можно и так
#        Result = u"""
#            (ID:%s) (Status:%s)
#            Накладная
#            %s
#            Итого: %s
#            """ % (self._identificator, self._status, Posit, self.itogo)
            
        return Result

    @classmethod
    def create_table(self):
        #TODO: 1. Автоматически вычислять SQL-команду создания таблицы
        #TODO: 2. Выполнять журналирование 
        #         Создаём таблицу по базовому документу
        try :
            mDocuments.Document.create_table()
        except sqlite3.OperationalError as Ex:         
            #TODO: Здесь записать ошибку в журнал
            print Ex.message

        print u"Creating Nakladnay table"
        #Создаём соединение
        conn = sqlite3.connect(os.path.expanduser(u"~/data.db"))
        curr = conn.cursor()
        curr.execute(
           """
           create table t_nakladnay (
                r_id_document integer not   null primary key references t_document ( i_id ) ,
                f_itogo       numeric(22,2) null 
           );
           """
            )
        #Сохраняем изменения 
        conn.commit()  
        #закрываем соединение      
        conn.close()
        
        mNakPos.NakPosition.create_table()          
            
################################################################################    
if __name__ == "__main__" :
    Nakl = create()
    print u"Status = ", Nakl.status
    print u"ID     = ", Nakl.identificator
    print u"Itogo  = ", Nakl.itogo
    
    try :
        Nakl = mDocuments.load( u"Vasay Pupkin 178265437153467" )
    except ValueError :
        print u"ValueError"
        Nakl = mDocuments.load( 1 )
        print u"Status = ", Nakl.status
        print u"ID     = ", Nakl.identificator
        Nakl = mDocuments.load( u"123" )
        print u"Status = ", Nakl.status
        print u"ID     = ", Nakl.identificator
        
        
        
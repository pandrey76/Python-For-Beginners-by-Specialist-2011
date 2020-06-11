#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os.path
'''
Created on 12.03.2012

@author: Prapor
'''

#Здесь мы не боимся называть класс исключений
#распространённым словом Error, т.к. наш класс фактически 
#называется mDocuments.Error, т.е. класс определен в модуле
  
class Error ( Exception ):
    #__buildin__ - название модуля(пространство имён) для всех встроенных классов Pythona
    #поэтому по факту мы записываем __builtin__.Exception
    pass
class NotFound( Error ):
    pass
    
def create ():
    '''
        Create new Document
    '''
#Если мы передаем второй параметр, который имеет значение по 
#умолчанию то его надо передавать с ключевым словом
    return Document(status = Document.New)

def load (Iden):
    '''
        Load Document from database
    '''
##    Doc = Document(id = Iden)
    Doc = Document(id = Iden)
    Doc.restore()
    return Doc

class Document(object):
    '''
    classdocs
    persistent object
    '''
    New = 1
    Status_Allowed = [ New ] 


##первый способ
##    def __init__(self, id = None, status = None, **kwargs):
##        '''
##        Constructor
##        '''
##        self.__Id = None
##        self.__Status = None
##        if id != None :
##            self.__Id = int( id )
##        if status != None :
##            if status not in Document.Status_Allowed :
##                raise ValueError
##            self.__Status = status

#Способ с наследованием 
    def __init__(self, **kwargs) :
        #TODO: 1. Запоминать значения других параметров
        #TODO: но никак их не обрабатывать.
        #  ID у документа появляется только после того,
        #  как он сохраняется в базе, у новых документов ID
        #  отсутствует, а у старых пресутствует
        ##self.__Id = None
        self.__Status = None        
        if "id" in kwargs :
            self.__Id = int( kwargs["id"] )
        if "status" in kwargs :
            if kwargs["status"] not in Document.Status_Allowed :
                raise ValueError
            self.__Status = kwargs["status"]

    #Функция property в качестве параметра принемает метод и возврашает
    #метод. Такие функции называются декораторами 
    identificator = property ( lambda self: self.__Id)
    
#''' таже самая запись
#    def getID (self):
#        return self.__Id
#    id = property (getID)
#'''     

    @property
    def _identificator(self):
        try :
            return self.identificator
        except AttributeError :
            return None
    
    @property
    def status (self ) :
        return self.__Status
    
    @status.setter
    def status (self, value ) :
        self.__Status = value
        if self.__Status == None :
            del self.__Status
    
    @property
    def _status(self):
        try :
            return self.status
        except AttributeError :
            return None
        
    @staticmethod    
    def connect ():
        #Дескриптор соединения с базой является менаджером контекста
        path = os.path.expanduser(u"~/data.db")
        return sqlite3.connect( path )
              
    def _save (self, conn):
        curr = conn.cursor()
            
        try :
                
            curr.execute(
                    """
                        update t_document
                        set   f_status = ?
                        where i_id     = ?
                     """, (self.status, self.identificator)
                     #Добавляется картеж ( self.status, self.identificator )
                     )
                #Если документ новый у него отсутствует ID, то выкинется исключение
                
        except AttributeError :
                 
            curr.execute(
                    """
                        insert into t_document ( f_status )
                            values ( ? )
                     """, ( self.status, )
                     )
                #Любые БД пердусматривают возможность при добавлении 
                #объекта (insert) возвратить его ID.
                #В MS SQL для этого есть специальная переменная "@@~"
                #В Postgre SQL можно особым образом написать поманду insert для этого есть специальная переменная "@@"
                #так как SQLite однопользовательская БД, то нужный нам 
                #ID будет последним.
                #Берём ID из базы. 
            curr.execute(
                    """
                        select max(i_id) from t_document
                     """
                     )
            for (iden,) in curr :
                self.__Id = iden

        
    def save (self): 
        with Document.connect( ) as conn :
            self._save(conn)
                   
    
    def restore (self):
        # TODO: Проверить неизменность типа документа
        with Document.connect( ) as conn :
            curr = conn.cursor()
            
            curr.execute(
                """
                    select f_status
                    from t_document
                    where i_id = ?
                """, ( self.identificator, )                
                )
            for ( status, ) in curr :
                self.__Status = status
                #Если status кривой, то БД возвращает None 
                if status == None :
                    #При попытке удалить не существующий аттрибут
                    #будет сгенерировано исключение Attributeerror.
                    del self.status
                return
            raise NotFound()
                    
                             

    
#Данный метод не является чисто статическим методом класса,
#т.к. в методе мы создаём конкретные таблицы, зависящие
#от структуры класса
#    @staticmethod
#    def create_table(): 
    @classmethod
    def create_table(self):
        #TODO: 1. Автоматически вычислять SQL-команду создания таблицы
        print u"Creating documents table"
        #Создаём соединение
        with Document.connect( ) as conn : 
            curr = conn.cursor()
            curr.execute(
               """
                   create table t_document (
                     i_id     integer not null primary key autoincrement ,
                     f_status integer     null                           ,
                     f_kind   integer     null -- 1- тип документа (накладная)
                   );
               """
               )

        #При использовании менаджера контекстане не надо явно
        #вызывать методы сохранение изменений Базы conn.commit() и
        #закрывытие соединения conn.close(), но при этом 
        #надо понимать, что если из блока менаджера контекста
        #будет сгенерированно исключение,то менаджер контекста
        #не произведёт операции сохранения изменений и закрытие базы       
        
if __name__ == "__main__" :
    D = create()
    print u"Status = ", D.status
    print u"ID     = ", D.identificator
    
    try :
        D = load( u"Vasay Pupkin 178265437153467" )
    except ValueError :
        print u"ValueError"
        D = load( 1 )
        print u"Status = ", D.status
        print u"ID     = ", D.identificator
        D = load( u"123" )
        print u"Status = ", D.status
        print u"ID     = ", D.identificator

        

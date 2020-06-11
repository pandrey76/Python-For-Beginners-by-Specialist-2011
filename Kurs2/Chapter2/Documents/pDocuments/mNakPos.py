#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os.path

'''
Created on 12.03.2012

@author: Prapor
'''
class NakPosition ( object ) :
    
    def __init__ (self):
        # TODO : 1. Конструктор должен принимать необязательные параметры
        # TODO :    id, title, unit, amount, price, summa
        pass
#Тоже общепринятая запись для свойств, если свойство простое
#и не требует дополнительных вычислений
#-------------------------------------#   
    ident  = property( lambda self: self.__Id     )
    #Если добавить ещё одну функцию после self.__Id, например set_id,
    #то это было бы свойство на чтения и запись и при записи будет вызвана функция set_id.                                                    
#-------------------------------------#    
#Свойство обёртка на случай если внутренний параметр отсутствует
#############################
    @property
    def _ident(self):
        try :
            return self.ident
        except AttributeError :
            return None
#############################        

#Старый способ определения свойств
#-------------------------------------#   
    def get_title (self):
        return self.__Title
    
    def set_title (self, title):
        self.__Title = unicode ( title )
        
    def del_title(self):
        del self.__Title
        
    title = property( get_title, set_title, del_title )
#-------------------------------------#

#Свойство обёртка на случай если внутренний параметр отсутствует
#############################
    @property
    def _title(self):
        try :
            return self.title
        except AttributeError :
            return None
#############################        

#Новый способ определения свойств
#-------------------------------------#   
    @property
    def unit(self):
        return self.__Unit
    
    @unit.setter
    def unit(self, un):
        self.__Unit = unicode(un)
         
    @unit.deleter
    def unit(self):
        del self.__Unit
#-------------------------------------#        
#Свойство обёртка на случай если внутренний параметр отсутствует
#############################
    @property
    def _unit(self):
        try :
            return self.unit
        except AttributeError :
            return None
#############################        

    @property
    def price(self):
        return self.__Price
    @price.setter
    def price(self,pr):
        self.__Price = int(pr)
    @price.deleter
    def price(self):
        del self.__Price

#Свойство обёртка на случай если внутренний параметр отсутствует
#############################
    @property
    def _price(self):
        try :
            return self.price
        except AttributeError :
            return None
#############################        
        
    @property
    def amount(self):
        return self.__Amount
    @amount.setter
    def amount(self,am):
        self.__Amount = long(am)
    @amount.deleter
    def amount(self):
        del self.__Amount

#Свойство обёртка на случай если внутренний параметр отсутствует
#############################
    @property
    def _amount(self):
        try :
            return self.amount
        except AttributeError :
            return None
#############################        
        
    @property
    def summa(self):
        try :
            return self.__Summa
        except AttributeError :
            return self.amount + self.price

    @summa.setter
    def summa(self,su):
        self.__Summa = long(su)
 
    @summa.deleter
    def summa(self):
        del self.__Summa
#Если мы удаляем сумму из позиции по накладной, если у нас указано количество
#и цена это означает, что мы сумму написали от балды, и это значение от балды будет удалено
#и при попытке получить значение суммы это значение будет вычисляться "return self.amount + self.price"
            
#Свойство обёртка на случай если внутренний параметр отсутствует
#############################
    @property
    def _summa(self):
        try :
            return self.summa
        except AttributeError :
            return None
#############################        

    def __unicode__(self):
        return u"%s,%s,%s,%s,%s,%s" % (
                self._ident,
                self._title,
                self._unit,
                self._price,
                self._amount,
                self._summa,
                )
    @classmethod
    def create_table(self):
        #TODO: 1. Автоматически вычислять SQL-команду создания таблицы
        print u"Creating documents table"
        #Создаём соединение
        conn = sqlite3.connect(os.path.expanduser(u"~/data.db"))
        curr = conn.cursor()
        curr.execute(
           """
           create table t_position (
                i_id           integer   not null primary key autoincrement ,
                r_id_nakladnay integer   not null references t_nakladnay( i_id_document ) ,
                f_ordinal      integer   not null ,
                f_title        text          null ,
                f_unit         text          null ,
                f_amount       integer       null ,
                f_price        numeric(33,4) null ,
                f_summa        numeric(22,2) null
           );
           """
            )
        #Сохраняем изменения 
        conn.commit()  
        #закрываем соединение      
        conn.close()          
        
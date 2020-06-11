#!/usr/bin/env python -O
# -*- coding: utf-8 -*-

import MyPack

a0 = input( u"a= ")
a1 = input( u"b= ")
a2 = input( u"c= ")

##############################    
try :
#Для вызова функции из модуля пишется вначале имя пакета
#Если в файле MyPack\__init__.py модуль msq_new импортируется
#так import msq_new, то вызов надо осуществлять так
    X= MyPack.msq_new.sqeq( a0, a1, a2 )    
    print X
#Если в файле MyPack\__init__.py модуль msq_new импортируется
#так from msq import sqeq, то вызов можно надо осуществлять так
    X= MyPack.sqeq( a0, a1, a2 )    
    print X

#Вызов явно импортированной закрытой переменной _A    
#    print MyPack.DD
#или    
    print MyPack.msq_new._A
    
except Exception as Exc :
    print type( Exc )
    raise 
finally :
    print u"END"

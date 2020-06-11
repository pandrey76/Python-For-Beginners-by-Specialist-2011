#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Файл модуля в Python является исполняемым, т.е. его можно
# запустить как основную программу
#Команда импорта будет выполнять все инструкции последовательно
#т.е в данном случае выполнит следующие инструкции
# 1  import math
# 2  Создаст функцию sqeq
import msq

a0 = input( u"a= ")
a1 = input( u"b= ")
a2 = input( u"c= ")

##############################    
try :
#Для вызова функции из модуля пишется в начале имя модуля
    X= msq.sqeq( a0, a1, a2 )    
    print X
except Exception as Exc :
    print type( Exc )
    raise 
finally :
    print u"END"

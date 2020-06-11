#!/usr/bin/env python
# -*- coding: utf-8 -*-  

#Файл модуля в Python является исполняемым, т.е. его можно
# запустить как основную программу

import math

#Чтобы скрыть переменную от внешнего мира к переменной добавляется перфикс
_A = [ 1, 2, 3  ]

def sqeq( a, b, c ) :
    try :
        D = b*b - 4*a*c
        if D < 0 :
            return [ ] 
        else :
            x1 = ( -b + math.sqrt( D ) ) / ( 2 * a )
            x2 = ( -b - math.sqrt( D ) ) / ( 2 * a )
            return [ x1, x2 ]
    except ZeroDivisionError :
        x1 = -c / b
        return [ x1, None ]
        
if __debug__ :
#    print u"Module " + __name__ + " imported"
    print u"Module", __name__, "imported"

#Тестовые команды будут выполнятся только если модуль 
#будет запущен на исполнение, т.е python.exe msq.py
#При импорте модуля из другого интерпретированного файла
if __name__ == "__main__"  :  
    print sqeq( 1, -5, 6 ) 
    print sqeq( 2, -10, 12 )
    print sqeq( 0, 2, 3 )
    print sqeq( 1, -5, 200 )  
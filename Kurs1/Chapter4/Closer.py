#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
def sqeq( a = 1.0, b = 2.0, c = 0.0 )  :
#    if type(a) == float
#    if type(a) in [ float, int ] #можно ннаписать так но мы не решим 
#                                 ошибку с целочисленным делением 
#Проверка для a
    if isinstance( a, int ) :
        a= float( a )
#    elif not isinstance( a, float ) : #можно и так
    else :
        if not isinstance( a, float ) :
            raise TypeError()
        
#Проверка для b
    if isinstance( b, int ) :
        a= float( b )
#    elif not isinstance( b, float ) : #можно и так
    else :
        if not isinstance( b, float ) :
            raise TypeError()
            
#Проверка для c
    if isinstance( c, int ) :
        a= float( c )
#    elif not isinstance( c, float ) : #можно и так
    else :
        if not isinstance( c, float ) :
            raise TypeError()

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
#Функция замыкания
##############################
sqeq1 = lambda b, c : sqeq( 1.0, b, c )
##############################
a0 = input( u"a= ")
a1 = input( u"b= ")
a2 = input( u"c= ")

##############################    
#Задание значения в виде списка
def test1 ( a, b, c = 0 ) :
    return a*b*c
    
X = test1( a0, a1, a2 )
print X
List = [ a0, a1, a2 ]
X = test1( *List )
print X
List1 = [ a0, a1 ]
X = test1( *List1 )
print X
List2 = [ a2 ]
#X = test1( *List2 ) #Ошибка т.к. второй параметр по умолчанию не задан
X = test1( a0, *List1 )
print X
#X = test1( *List1,  *List2 ) Ошибка так писать нельзя 
X = test1( a0, a1,  *List2 )
print X

##############################    
##############################    
#Превращаем кортеж в список
##############################    
#1 Способ
T = (a0, a1, a2 )
List10 = [ x for x in T ]
print u"List10 = ", List10
X = test1( *List10 )
print u"List10 = ", List10
print X

#2 Способ Используют гораздо чаще
# В частности при работе с базой данных
Dict = {
        u"a" : a0,
        u"b" : a1,
        u"c" : a2 
       }
#При этом параметры будут переданы по ключевым словам ( a, b, c )
X = test1( **Dict )
print u"Dict = ", Dict
print X
##############################    
try :
#    X= sqeq( 1.0, a1, a2 )
#Замыкание
    X= sqeq1( a1, a2 )
    print X
#Задание значений по умолчанию
##############################
    X= sqeq( 1.0, a1 )    
    print X
    X= sqeq( a0 )    
    print X
    X= sqeq( )    
    print X
##############################
#Задание значения по ключевым словам
##############################
    X= sqeq( a = a2, c = a0 )
    print X
##############################
    X= sqeq( a = a2, c = a0 )
    print X
##############################    

except Exception as Exc :
    print type( Exc )
    raise 
finally :
    print u"END"

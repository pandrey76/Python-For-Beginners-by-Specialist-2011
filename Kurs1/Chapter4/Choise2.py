#!/usr/bin/emv python
# -*- coding: utf-8 -*-

import math
def sqeq( a, b, c ) :
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
        
a0 = input( u"a= ")
a1 = input( u"b= ")
a2 = input( u"c= ")

try :
    X= sqeq( a0, a1, a2 )
    print X
except Exception as Exc :
    print type( Exc )
    raise 
finally :
    print u"END"
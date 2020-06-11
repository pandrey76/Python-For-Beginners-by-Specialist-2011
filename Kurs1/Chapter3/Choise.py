#!/usr/bin/env python
# -*- coding: utf-8 -*-

#if A < 0 and B > C :
#    JGKLFDJGKLJFDKLGJFD
#    FDLLDLDKFGDFKGL
#else
#    kldjgskljf
#    dfgdkgkdgkd
#sklfdjgsdjf
# klfdjgd

import math
#Уравнение вида: a*x*x + b*x + c = 0
#Решим уравнение1: x*x - 5 * x + 6 = 0
#Решим уравнение2: x*x + 5 * x + 200 = 0
a = input( u"a= ")
b = input( u"b= ")
c = input( u"c= ")

D = b*b - 4*a*c
if D < 0 :
    print u"No Solutions" 
else :
    x1 = ( -b + math.sqrt( D ) ) / ( 2 * a )
    x2 = ( -b - math.sqrt( D ) ) / ( 2 * a )
    print u"x1 = ", x1
    print u"x2 = ", x2
    
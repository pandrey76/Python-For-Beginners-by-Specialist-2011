#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = [ 1,2,3]
y = x
print u"y = ", y

x[2] = u"Vasya Pupkin"
print u"x = ", x
print u"y = ", y

a = 2
b = a
 
print u"a = ", a
print u"b = ", b
a = 56
print u"a = ", a
print u"b = ", b

#q = ( a < b and b < c ) or d != f(x) (q = True /False)

c = u"Vasay"
print u"c = ", c
c = c[:3] + u"d" + c[3:]
print u"c = ", c
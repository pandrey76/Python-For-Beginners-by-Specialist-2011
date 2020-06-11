#!usr/bin/env python
# -*- coding: utf-8 -*-

print u"Hello, word!"
x = 3
print type(x)

z = u"hello"
print type ( z )

a = 29.96
print type ( a ) 

y = 333333333
print type ( y )

yy = y * y * y * y * y * y * y
print type ( yy )
print u"yy = ", yy

#print u"Hello" + 25    Error
print u"Hello" + unicode(25)

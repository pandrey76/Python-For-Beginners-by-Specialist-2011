#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib


#Алгоритм хэширования md5
HS = hashlib.md5()
HS1 = hashlib.sha1()

#замыкание на объект HS1
#Этот способ часто используется при обработки событий
func = HS1.update

with open ( u"file.txt", u"rb" ) as TRG :
    try :
        while True :    
            A = TRG.read ( 1024 )
            if A == '' : break
            HS.update( A )
#Вызов метода HS1.update
            func( A )
#Команды "pass" - ничего не делает            
#В данном случае мы гасим исключения
    except : pass
#CRC - в бинарном виде.
print HS.digest()  
#CRC - в шестнадцатиричном виде.
print HS.hexdigest()            

print HS1.digest()  
print HS1.hexdigest()            
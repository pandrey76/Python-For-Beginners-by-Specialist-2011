﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs
import random
#Заменяем телефон вопросиками
def false_phone1( match ) :
    return u"+?(???)???-??-??"

#Заменяем телефон случайными данными
def false_phone2( match ) :
    D = [ u"0", u"1", u"2", u"3", u"4",
          u"5", u"6", u"7", u"8", u"9", ] #Питон допускает в словарях и списках запятую в конце
    R = u"";
    for k in range(0, 11) :
        R += D[random.randrange(0, len(D))]
    return u"+"+R[:1]+u" ("+R[1:4]+u") "+R[4:7]+u"-"+R[7:] 

#Заменяем телефон случайными данными, а код страны связи оставляем какой был
#код оператора меняет случайно на другой из списка и остальные 7 цифр генерит случайно
def false_phone3( match ) :
    D = [ u"0", u"1", u"2", u"3", u"4",
          u"5", u"6", u"7", u"8", u"9", ] #Питон допускает в словарях и списках запятую в конце
    Op = [
            [ u"916", u"915", u'985' ],
            [ u"925", u"926"         ],
         ]   
    R = u"+"+match.group(1)
    O = match.group(2)
    for OpCodes in Op :
        if O in OpCodes :
            N = random.randrange(0,len(OpCodes))
            O = OpCodes[N]
    R += u"(" + O + u")"
    for k in range(0, 3) :
        R += D[random.randrange(0, len(D))]
    R += u"-"
    for k in range(0, 4) :
        R += D[random.randrange(0, len(D))]

    return R 

CD = codecs.lookup( u"cp866" )

X = CD.decode( raw_input() )[0]
print X

#Создаём патерн
PT1 = re.compile( ur"\d{3}" )

M1 = PT1.search( X )
#if M != None :
#    pass    #Команда pass пишется в тех местах где мы хотим что то написать.
if M1 :
    print u"Ок."
else :
    print u"Строка не соответствует паттерну."

#Создаём патерн
PT2 = re.compile( ur"[+]7\((\d{3})\)" )
M2 = PT2.search( X )
if M2 :
# Ввод: вася пупкин +7(496)568-07-97    
    print M2.group(0)   #результат для PT2: +7(496)
    print M2.group(1)   #результат для PT2: 496
else :
    print u"Строка не соответствует паттерну."
    
#Создаём патерн
PT3 = re.compile( ur"[+]7\((\d{3})\)(\d{3}-\d{2}-\d{2}|\d{3}-\d{4}|\d{7})" )

M3 = PT3.search( X )
if M3 :
# Ввод: вася пупкин +7(496)568-07-97    
    print M3.group(0)   #результат для PT3: +7(496)568-07-97
    print M3.group(1)   #результат для PT3: 496
    print M3.group(2)   #результат для PT3: 568-07-97
else :
    print u"Строка не соответствует паттерну."

#Создаём патерн
PT4 = re.compile( ur"[+]7\((\d{3})\)(\d{3}-(\d{2}-\d{2}|\d{4})|\d{7})" )

M4 = PT4.search( X )
if M4 :
# Ввод: вася пупкин +7(496)568-07-97    
    print M4.group(0)   #результат для PT4: +7(496)568-07-97
    print M4.group(1)   #результат для PT4: 496
    print M4.group(2)   #результат для PT4: 568-07-97
    print M4.group(3)   #результат для PT4: 07-97  Если вход: вася пупкин +7(496)5680797, то результат None     
    print M4.groups()   #результат для PT4: (u'496', u'568-07-97', u'07-97')
 
    #Метод start определяют номер символа соответствующая началу группы в исходной строке.
    #Метод end определяют номер символа соответствующая концу группы в исходной строке.
    #Единственный параметр методов - номер соответсвующей группы.
    print M4.start(1)   #результат для PT4: 15
    print M4.end(1)     #результат для PT4: 18
    print M4.start(3)   #результат для PT4: 23
    print M4.end(3)     #результат для PT4: 28
    
    #Удаляем из М4 2 группу 
#    X = X[:M4.start(2)] + X[M4.end(2):] 
#    print X     #результат +7(496)
    X1 = X[:M4.start(2)] + X[M4.end(2):] 
    print X1     #результат +7(496)
    #Получаем картеж из начального номера символа группы из исходной строки и
    #последнего символа группы из исходной строки
    print M4.span(1)    #результат (15, 18)
    
else :
    print u"Строка не соответствует паттерну."

#Создаём патерн
PT5 = re.compile( ur"\+(7)\((\d{3})\)(\d{3})(-)(\d{2}-\d{2}|\d{4}|\d{7})" )

M5 = PT5.search( X )
if M5 :
# Ввод: вася пупкин +7(496)568-07-97    
    print M5.group(0)   #результат для PT5: +7(496)568-07-97
    print M5.group(1)   #результат для PT5: 7    
    print M5.group(2)   #результат для PT5: 496
    print M5.group(3)   #результат для PT5: 568
    print M5.group(4)   #результат для PT5: -
    print M5.group(5)   #результат для PT5: 07-97
    print M5.groups()   #результат для PT5: (u'7', u'496', u'568', u'-', u'07-97')
 
    #Осуществляем замену в соответствии с шаблоном замены
    Y = PT5.sub(ur"+\g<1>(\2)XXX\g<4>XXXX", X)
    print Y     #результат: вася пупкин +7(496)XXX-XXXX

    #Функция sub принимает в качестве замены функцию, здесь мы видим использование функции как объекта первого класса.
    Y1 = PT5.sub(false_phone1, X)
    print Y1    #результат: вася пупкин +?(???)???-??-??     
    Y2 = PT5.sub(false_phone2, X)
    print Y2    #результат: вася пупкин +9 (088) 185-2035     
    Y3 = PT5.sub(false_phone3, X)
    print Y3    #результат: вася пупкин +7(985)349-6154     
    
    #Метод start определяют номер символа соответствующая началу группы в исходной строке.
    #Метод end определяют номер символа соответствующая концу группы в исходной строке.
    #Единственный параметр методов - номер соответсвующей группы.
    print M5.start(1)   #результат для PT5: 13
    print M5.end(1)     #результат для PT5: 14
    print M5.start(3)   #результат для PT5: 19
    print M5.end(3)     #результат для PT5: 22
    
    Z = re.escape ( "c:\Pathlen\python.txt" ) #как и везде экранирует строку,
                              #т.е. превращает полученную строку в патерн регулярного выражения
    print Z #результат: c\:\\Pathlen\\python\.txt
else :
    print u"Строка не соответствует паттерну."


PT6 = re.compile( ur"\s*[,;]\s*" ) #патерн разделитель
A = PT6.split( u"Vasya, Petya      ; Николай" )    
print A #результа [u'Vasya', u'Petya', u'\u041d\u0438\u043a\u043e\u043b\u0430\u0439']
    
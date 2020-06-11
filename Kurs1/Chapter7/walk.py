#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

Cdrive = u"c:\\"
#Обход берева каталогов
#walk это генератор - функция которая возвращает кортеж из трёх элементов

for ( path, dirs, files ) in os.walk( Cdrive ) :
    #path - та точка в дереве каталогов где она находится в данный момент.
    #dirs - это список всех папок находящихся под этой точкой.
    #files - это список всех файлов находящихся под этой точкой.

#Задача обойти все папки кроме папкок "Application Data".    
    #Так как в Python все переменные являются ссылками на значения, то переменные 
    #path, dirs и files являются ссылками на значения определёнными в генератор функции "walk"
    #и удалив параметр "Application Data" из списка dirs, и таким образом мы удалили папку из дальнейшего поиска.
    
    if u"Application Data" in dirs :
        dirs.remove ( u"Application Data" )
        #или
        #del dirs[ dirs.index( u"Application Data" ) ]
    if u"Distr" in dirs :
        dirs.remove ( u"Distr" )
    #print path
    
    for File in files :
        P = os.path.join ( path, File )
        #преобразуем абсолютный путь в относительный
        print os.path.relpath ( P, Cdrive )
        

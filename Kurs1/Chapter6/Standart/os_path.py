﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Работает со строками пердставляющие пути к файлам
import os.path



#os.path.split - разделяет на путь к папке и имя файла
X = u"d:\\Distr\\All Distibutives\\Обучение\\Программирование\\Языки\\Python\\Видео\\Python. Специалист\\Уровень 1. Основы программирования [2011, RUS]\\Python. Уровень 1. Основы программирования\\WORK.zip"
########################################################
print os.path.split ( X )
#результат:
#(u'd:\\Distr\\All Distibutives\\\u041e\u0431\u0443\u0447\u0435\u043d\u0438\u0435\\\u041f\u0440\u043e\u0433\u0440\u0430\u
#u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435\\\u042f\u0437\u044b\u043a\u0438\\Python\\\u0412\u0438\u0434\u
#u0435\u043e\\Python. \u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\\\u0423\u0440\u043e\u0432\u0435\u043d\u
#u044c 1. \u041e\u0441\u043d\u043e\u0432\u044b \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0
#u430\u043d\u0438\u044f [2011, RUS]\\Python. \u0423\u0440\u043e\u0432\u0435\u043d\u044c 1. \u041e\u0441\u043d\u043e\u0432\
#u044b \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f', u'WORK.zip')
########################################################

########################################################
W = os.path.basename ( X )
print W
#результат:
#WORK.zip
########################################################

########################################################
V = os.path.dirname  ( X )
print V
#результат:
#d:\Distr\All Distibutives\Обучение\Программирование\Языки\Python\Видео\Python. Специалист\Уровень 1. Основы программиров
#ания [2011, RUS]\Python. Уровень 1. Основы программирования
########################################################

########################################################
print os.path.join ( V, W )
#результат:
#d:\Distr\All Distibutives\Обучение\Программирование\Языки\Python\Видео\Python. Специалист\Уровень 1. Основы программирования [2011, RUS]\Python. Уровень 1. Основы программирования\WORK.zip
########################################################

########################################################
print os.path.exists ( X )
#результат:
#True
########################################################

########################################################
print os.path.isfile ( X )
#результат:
#True
print os.path.isfile ( V )
#результат:
#False
print os.path.isfile ( u"test" )
#результат:
#False
########################################################

Y1 = u"d:\Distr\All Distibutives\Обучение\Программирование\Языки\Python\..\СИ\Программирование на языке C (Си)\viewtopic.php_files\erle_data\index_data\..\..\rutracker_top_data\swfobject.js"
Y = u"d:\\Distr\\All Distibutives\\Обучение\\Программирование\\Языки\\Python\\..\\СИ\\Программирование на языке C (Си)\\viewtopic.php_files\\erle_data\\index_data\\..\\..\\rutracker_top_data\\swfobject.js"
########################################################
#Перевод относительного пути к абсолютному
Z = os.path.normpath ( Y1 )
print Z
#результат: Почему то не правильно работает 
#d:\Distr\All Distibutives\Обучение\Программирование\Языки\СИ\Программирование на языке C (Си)♂iewtopic.php_files\erle_da
#utracker_top_data\swfobject.js
print os.path.isfile ( Z )
#результат: 
#False
Z = os.path.normpath ( Y )
print Z
#результат: Почему то не правильно работает 
#d:\Distr\All Distibutives\Обучение\Программирование\Языки\СИ\Программирование на языке C (Си)\viewtopic.php_files\rutrac
#ker_top_data\swfobject.js

print os.path.isfile ( Z )
#результат: 
#True

########################################################

########################################################
#Перевод относительного пути к абсолютному
print os.path.abspath ( X )
#результат: 
#d:\Distr\All Distibutives\Обучение\Программирование\Языки\Python\Видео\Python. Специалист\Уровень 1. Основы программиров
#ания [2011, RUS]\Python. Уровень 1. Основы программирования\WORK.zip
########################################################

########################################################
#Перевод абсолютного к относительному
print os.path.relpath ( X )
#результат: 
#..\..\..\Distr\All Distibutives\Обучение\Программирование\Языки\Python\Видео\Python. Специалист\Уровень 1. Основы програ
#ммирования [2011, RUS]\Python. Уровень 1. Основы программирования\WORK.zip
print os.path.relpath ( X, u"d:\Distr\All Distibutives" )
#результат: 
#Обучение\Программирование\Языки\Python\Видео\Python. Специалист\Уровень 1. Основы программирования [2011, RUS]\Python. У
#ровень 1. Основы программирования\WORK.zip
########################################################

########################################################
#Пути профайла конкретного юзера
print os.path.expanduser ( u"d:\Distr\All Distibutives" )
#результат: Функция ничего не делает
#d:\Distr\All Distibutives
print os.path.expanduser ( u"~\WORK" )
#результат: Функция ничего не делает
#C:\Users\Prapor\WORK
########################################################

########################################################
#Функция поставляет в строку переменную окружения
#для получения значения переменной среды используется  следующий способ
print os.path.expandvars ( u"${PATH}" )
#результат: Значение переменной среды: PATH
#C:\Perl64\site\bin;C:\Perl64\bin;C:\Program Files (x86)\AMD APP\bin\x86_64;C:\Program Files (x86)\AMD APP\bin\x86;C:\Win
#dows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\ATI
# Technologies\ATI.ACE\Core-Static;C:\Program Files (x86)\Microsoft SQL Server\90\Tools\binn\;c:\Program Files (x86)\Micr
#osoft Visual Studio 9.0\Common7\IDE\;c:\Windows\Microsoft.NET\Framework\v2.0.50727\;c:\Program Files\Microsoft SDKs\Wind
#ows\v6.0A\Bin\

#Так как перемнные окружения иногда являются ссылками на другие переменные окружения. Если использовать словарь os.envar
#то переменные окружения будут получены в виде описанном в файле конфигурации. При получении переменной среды через expandvars
#модуля os.path она будет развёрнута доконца и все возможные в неё подстановки будут выполнены.
########################################################

########################################################
#Функция возвращают список файлов
print os.listdir ( V )

#V = d:\Distr\All Distibutives\Обучение\Программирование\Языки\Python\Видео\Python. Специалист\Уровень 1. Основы программиров
#ания [2011, RUS]\Python. Уровень 1. Основы программирования

#результат:
#[u'2011-01-17_18.38_PITON1_17_01_28_01_PL_v.wmv', u'2011-01-18_18.36_PITON1_17_01_28_01_PL_v.wmv', u'2011-01-19_18.48_PI
#TON1_17_01_28_01_PL_v.wmv', u'2011-01-20_18.30_PITON1_17_01_28_01_PL_v.wmv', u'2011-01-21_18.38_PITON1_17_01_28_01_PL_v.
#wmv', u'2011-01-24_18.34_PITON1_17_01_28_01_PL_v.wmv', u'2011-01-25_18.51_PITON_17_01_28_01_PL_v.wmv', u'2011-01-26_18.3
#7_PITON1_17_01_28_01_PL_v.wmv', u'2011-01-27_18.40_PITON1_17_01_28_01_PL_v.wmv', u'2011-01-28_18.32_PITON1_17_01_28_01_P
#L_v.wmv', u'WORK.zip']

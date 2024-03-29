﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
#модуль работы с данными разделенными ","
#Если в тексте встречается запятая её записывают в ковычки ""
#Если встречаются символ ковычки, то её экранируют "/" или дважды указывают ковычку
#К сожалению для формата CSV нет единого стандарта, например первые пять значений 
#разделенные запятой принимаются как отдельные данные, а после пятой запятой - шестое значение, 
#вне зависимости от того какие значения следуют
import csv

with codecs.open ( u"file1.txt", u"wb", 
                    encoding = u"windows-1251" ) as TRG:
#Вложенные не связанные менаджеры контентов обычно не используются, но допустимы
#    with csv.writer( u"file1.txt" ) as FMT :
    FMT = csv.writer ( TRG )
    FMT.writerow( [ u"Vasy", u"Pupkin", 120 ] )
    FMT.writerow( [u"Prapor", u"Vasiliy Ivanovich", 120] ) 


    
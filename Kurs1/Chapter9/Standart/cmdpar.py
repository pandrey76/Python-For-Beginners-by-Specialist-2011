#!/usr/bin/env python
# -*- coding: utf-8 -*-


#try

#Если Питон версии 3.0, то будет сгенерированно исключение ImportError
#т.к. в третей версии Питона отсутствует данный модуль
#для второй версии Питона данный модуль будет загружен    

#    import argparse

#except ImportError :

#Данный модуль определён в третьей версии Питона

#    import optparse

#оба модуля определены только в версии 2.7 и у этих модулей разные интерфейсы    

#Коммандная строка в данный момент стандартизирована
#Например: hg commit file1 file2 -m "Result"
        #hg commit - здесь не может быть опций 
        #-m - опции
        #"Result"- Имя запускаемой комманды.
        
#       --message="This is a message"        
#       --message "This is  a message"        

#       -m"This is a message"        
#       -m "This is a message"   

#   /m
#   -m     
#   +m

import optparse

parser1 = optparse.OptionParser()
parser1.add_option( u"-m", u"--message", 
                        dest=u"message",
                        action=u"store_true",#Если опция присутствует то она True                        
                        default=False,
                        help=u"Messgae to screen on screen" )
parser1.add_option( u"-c", u"--count", 
                        dest=u"count",
                        type=u"int",#Тип входных параметров
                        help=u"Count of peaple!" )

( options, args ) = parser1.parse_args( )

subcommand = args[0]
del args[0]
          
print subcommand          
print options
print args                         

#################################################
#Командная строка: c:\Python27\python.exe cmdpar.py param -m "This"
#Результат: {'message': 'This'}
#           ['param']
#################################################
#################################################
#c:\Python27\python.exe cmdpar.py -help
#Usage: cmdpar.py [options]

#Options:
#  -h, --help            show this help message and exit
#  -m MESSAGE, --message=MESSAGE
#                        Messgae to screen on screen
#################################################
#################################################
#c:\Python27\python.exe cmdpar.py --help
#Usage: cmdpar.py [options]

#Options:
#  -h, --help            show this help message and exit
#  -m MESSAGE, --message=MESSAGE
#                        Messgae to screen on screen
#################################################
#################################################
#c:\Python27\python.exe cmdpar.py
#{'message': None}
#[]
#################################################

( options, args ) = parser1.parse_args( )

print options
print args                         

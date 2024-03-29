﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Запуск команды из другой программы

#Первый способ Просто запускаем программу (Запуск другого процесса)
#os.system

#Второй способ
import os.path
import subprocess

######################################################
path = os.path.expandvars( u"%SystemRoot%\\system32\\notepad.exe" )
print path
#необходимо передавать полный путь к exe файлу
dir = subprocess.Popen( [path] )
#dir = subprocess.Popen( [ ], executable= u"dir" )
#dir = subprocess.Popen( [u"dir", u"/w"] )
print dir.poll ( )#poll возвращает текущее состояние объекта (Метод возвращает Код завершения процесса: None)
dir.wait ( )    #Ждем окончания процесса (Метод возвращает Код завершения процесса: None)
print dir.poll ( ) #(Метод возвращает Код завершения процесса: 0)
######################################################
######################################################
#path2 = os.path.expandvars( u"notepad.exe" )
path2 = path
print path2
#необходимо передавать полный путь к exe файлу
#dir2 = subprocess.Popen( [path2], cwd = "%SystemRoot%\\system32\\" ) #cwd - рабочая папка процесса

dir2 = subprocess.Popen( [path2], env = { "PATH": "c:\\"}) #передавать в качестве env не юникод строки, иначе будет ошибка
#Внимание!! С параметром env необходимо быть внемательным потому что существует возможность,
#что для процесса системные переменные среды будут не доступны. Поэтому если нам надо к системным переменным 
#окружения добавить свои, то необходимо воспользоваться словарём os.environ.

#dir = subprocess.Popen( [ ], executable= u"dir" )
#dir = subprocess.Popen( [u"dir", u"/w"] )
print dir2.poll ( )#poll возвращает текущее состояние объекта (Метод возвращает Код завершения процесса: None)
dir2.wait ( )    #Ждем окончания процесса (Метод возвращает Код завершения процесса: None)
print dir2.poll ( ) #(Метод возвращает Код завершения процесса: 0)
######################################################
######################################################
path3 = path
print path2
#необходимо передавать полный путь к exe файлу
#dir3 = subprocess.Popen( [path2], cwd = "%SystemRoot%\\system32\\" ) #cwd - рабочая папка процесса

dir3 = subprocess.Popen( [path3], env = { "PATH": "c:\\"}) #передавать в качестве env не юникод строки, иначе будет ошибка
#Внимание!! С параметром env необходимо быть внемательным потому что существует возможность,
#что для процесса системные переменные среды будут не доступны. Поэтому если нам надо к системным переменным 
#окружения добавить свои, то необходимо воспользоваться словарём os.environ.

#dir = subprocess.Popen( [ ], executable= u"dir" )
#dir = subprocess.Popen( [u"dir", u"/w"] )
print dir3.poll ( )#poll возвращает текущее состояние объекта (Метод возвращает Код завершения процесса: None)
dir2.wait ( )    #Ждем окончания процесса (Метод возвращает Код завершения процесса: None)
print dir3.poll ( ) #(Метод возвращает Код завершения процесса: 0)
######################################################


######################################################
import StringIO #не является файло подобным объектом

SRC = StringIO.StringIO ( u"Hello" );

dir4 = subprocess.Popen( [u"C:\\Python27\\python.exe", u"mod.py"],
                        stdin = subprocess.PIPE,
#                        stdin = SRC,
                        stdout = subprocess.PIPE )
#Кроме PIPE можно писать любой файло подобный объект    ( методы read, write )                    
P = dir4.communicate ( u"This is a test" )
print P
print dir4.poll ( )#poll возвращает текущее состояние объекта (Метод возвращает Код завершения процесса: None)
dir4.wait ( )    #Ждем окончания процесса (Метод возвращает Код завершения процесса: None)
print dir4.poll ( ) #(Метод возвращает Код завершения процесса: 0)
######################################################
######################################################

dir5 = subprocess.Popen( [u"C:\\Python27\\python.exe", u"mod.py"],
                        stdin = subprocess.PIPE,
                        stdout = subprocess.PIPE )
X = u""
while dir5.poll() == None :
#    sleep( 100 )
    ( cout, cerr ) = dir5.communicate ( "Hello")
    X += cout
                        
dir5.wait ( )    #Ждем окончания процесса (Метод возвращает Код завершения процесса: None)
print X
print dir5.poll ( ) #(Метод возвращает Код завершения процесса: 0)
######################################################

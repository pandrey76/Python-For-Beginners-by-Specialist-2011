﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Стандартный модуль sys

import sys

#Нам интересны три вещи

#1 
#Список содержит все параметры команндной строки
#В Python первый параметр argv это строка содержащая
#полный путь к интерпретируемому файлу
for P in sys.argv :
    print P 
#Для анализа параметров коммандной строки в самом Питоне 
#используется другой метод. А сисок sys.argv необходим
#для передачи  в стронние библеотеки.

#2
#Список переменных окружения, но для Winidows для некоторых версий
#операционных систем в данном списке возвращаются не глобальные
#переменные среды, а переменные среды пользователя.    
#Данный словарь используется для того, чтобы туда добавить ещё  
#пременные которые в ОС не сохраняться, а будут сохранениы до конца работы программы 
for P in sys.environ :
    print P
#3 
#Код завершения программы передаваемой интерпретатору, 
#чтобы он вернул даннй код завершения OS
sys.exit( 0 )
    
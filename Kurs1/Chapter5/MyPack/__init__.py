﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import msq_new
#импортируется только функция sqeq (рекомендуемая запись)
from msq_new import sqeq

#импортируется список функция sqeq и т.д. (рекомендуемая запись)
#from msq_new import sqeq, sqeq1, mtr, dd

#Можно но не рекомендуется использовать запись
#Данная запись разрешается только в файлк __init__.py
#данная запись импортирует все элементы модуля кроме тех которые
#начинаются со знака подчеркивания
#from msq_new import *

#Функции и переменные начинающиеся с подчёркивания должны импортироваться явно ( но это почему то не так )
#from msq_new import _A
#DD = _A
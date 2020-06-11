#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs


# 1. В Python параметр можно указаывать ключевым словом.
# 2. Tо что между скобками разрешается разбивать на две строки
# 3. Файл необходимо открывать в двоичном виде.
with codecs.open( u"file.txt", u"rb",
                encoding = u"windows-1251" ) as SRC :
    for Line in SRC :
        print Line
       
        
# -*- coding: utf-8  -*-
import cgi
import os
import sys
import codecs
storage = cgi.FieldStorage()
data = storage.getvalue('data')
data = str(data)
open('text.txt', 'w').close() #удаляем файл
if data is not None:
    f = codecs.open('text.txt', 'w', encoding='utf-8')
    f.write(data)
    f.close
    print("ok")


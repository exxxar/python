# -*- coding: cp1251 -*-
stroka = raw_input('введите url')
if stroka[0:3] == "www":
    stroka="http://"+stroka
if stroka[-4:] != ".com":
    stroka = stroka+".com"
print "Результат строки: "+stroka

# -*- coding: cp1251 -*-
stroka = raw_input('������� url')
if stroka[0:3] == "www":
    stroka="http://"+stroka
if stroka[-4:] != ".com":
    stroka = stroka+".com"
print "��������� ������: "+stroka

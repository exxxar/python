# -*- coding: cp1251 -*-
from math import *

try:
    a = float(raw_input('������� �����'))
    if (a<0):
        raise ValueError('����� �������������')
    arr = modf(a)
   # print arr[0]
    print('%d ��� %d ���')%(arr[1],arr[0]*100)
except ValueError,e:
    print e



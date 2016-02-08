# -*- coding: cp1251 -*-
from math import *

try:
    a = float(raw_input('Введите сумму'))
    if (a<0):
        raise ValueError('Число отрицательное')
    arr = modf(a)
   # print arr[0]
    print('%d руб %d коп')%(arr[1],arr[0]*100)
except ValueError,e:
    print e



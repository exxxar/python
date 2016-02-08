# -*- coding: cp1251 -*-
arr = range(10,100,1)
for el in arr:
    r1=el/10
    r2=el%10
    if r1+r2==7:
        print el

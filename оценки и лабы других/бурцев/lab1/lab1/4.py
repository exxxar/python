# -*- coding: cp1251 -*-
from math import *
n = int(raw_input('Кол-во слогаемых'))
flag =True
mypi =0.0
for i in range(1,n,2):
    if(flag):
        mypi+=1.0/i
        flag=False
    else:
        mypi-=1.0/i
        flag=True
mypi*=4
print "mypi = "+str(mypi)
print "pi = "+str(pi)
    

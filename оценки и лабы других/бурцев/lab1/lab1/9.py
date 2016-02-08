# -*- coding: cp1251 -*-
import math,random
f = lambda x:int(math.pow(2,x))
two=[]
for el in range(1,16):
    two.append(f(el))
print two
N = int(raw_input("Input N: "))
arrN=[random.randrange(1, 100) for i in range(N)]
print "До: "
print arrN
size=len(arrN)
m = 0
for el in two:
    if size==el:
        m=el
        break
    if size>el:
        m = el
    elif size<el:
        if abs(size-m)<abs(size-el):
            break
        else:
            m=el

count = abs(N- m)
#print count
while count != 0:
    count-=1
    arrN.append(0)
    
    
print "После: "
print arrN
    
        

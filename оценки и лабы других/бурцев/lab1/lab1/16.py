
# -*- coding: cp1251 -*-

from collections import Counter
import re
from numpy import *
infile = open('data1.txt', 'r')

arr=[];
for line in infile:
    arr+= re.findall('[A-Za-z]+',line)
    
print Counter(arr)



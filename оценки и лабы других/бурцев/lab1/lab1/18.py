# -*- coding: cp1251 -*-
import re
infile = open("data2.txt")
i=1
lists=[]
index=[]
count=1
for line in infile:
    
    lists+=re.findall(r'\d{3}\.\d{3}\.\d{1}\.\d{2}',line)
    
    if(lists):
        
        for el in lists:
            print "Номер строки: "+str(count)+ " Позиция: "+str(line.find(el))+ " Найдено \""+el+"\""
    lists=[]
    count+=1
infile.close()
    

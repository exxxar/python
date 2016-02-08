# -*- coding: cp1251 -*-
import os,hashlib

lists=[[]]
listdir = []
counts=[]
flag =True
for root, dirs, files in os.walk('D:\music2'):
    for one_file in files:
        listdir.append(os.path.join(root, one_file))
for el in listdir:
    
    f = open(el , 'r' )
    data = f. read()
    f. close()
    checksum = hashlib. md5(data). hexdigest()
    for lis in lists:
        if checksum in lis:
               lis.append(el)
               flag=False
               lis[1]+=1          
    if flag:      
        lists.append([checksum,1,el])
    flag=True
for el in lists[1:]:
     if el[1]>1:
         print "Хеш: "+el[0]+ "\nколичество файлов("+str(el[1])+")\n"+str(el[2:])+"\n ----------------"
         
     
     



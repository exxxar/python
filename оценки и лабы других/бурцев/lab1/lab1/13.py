# -*- coding: cp1251 -*-
try:
    #mystr=raw_input('Введите текст: ')
    mystr="Donetsk is, a - beautiful city."
    if(mystr[-1]!="."):
        raise ValueError('В конце должна быть точка')
    mylist = mystr.split()
    print mylist
    i=1
    newstr=""
    for el in mylist:
        
        if el[-1]=="." or el[-1]==",":
            newstr += el[0:-1]+"("+str(i)+")"+el[-1]+" "
            i=i+1
        elif el[-1]=="-":
            newstr +="- "
        else:
            newstr += el+"("+str(i)+") "
            i=i+1
    print newstr
    print mystr
except ValueError,e:
    print e

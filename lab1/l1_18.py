# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import re

def file2list(text_file):
    try:
        print text_file
        f = open(text_file)
    except IOError:
        print "file %s not exist" %text_file
        return 1

    mas_text = f.readlines()
 
    f.close()
    return mas_text

mas_text = file2list("c:\\1\\my_file.txt")
l = len(mas_text)
i = 0
rezult = []
while i<l:
    m = re.findall(r'\d{2}:\d{2}:\d{2}', mas_text[i])
    if m!=[]:   
        buf = [m,i,mas_text[i].index(m[0])]
        rezult.append(buf)
    i+=1
i=0
while i<len(rezult):
    print "stroka "+rezult[i][0][0]+" #"+str(rezult[i][1])+" pos="+str(rezult[i][2])
    i+=1
#print rezult    
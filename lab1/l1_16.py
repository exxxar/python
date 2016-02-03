
import re
#print [str(k) for k in re.findall(r'(\b[A-Z][a-z]+\d{2})\b', open('c:\\1\\my_file.txt', 'r' ).read())]
f = open('c:\\1\\my_file.txt', 'r')
mass = []
for line in f:
    str = re.findall(r'(\b[A-Za-z]+)\b',line)
    if str!=[]:
        mass.append(str)
char_m = []
i = 0
for i in range(255):
    m = ['',0]
    char_m.append(m)
    
for i in mass:
    for j in range(len(i)):
        for k in range(len(i[j])):
            char_m[ord(i[j][k])][0]=i[j][k]
            char_m[ord(i[j][k])][1]+=1
            #print char_m[ord(i[j][k])]

for i in char_m:
    for j in range(len(char_m)-1):
        if char_m[j][1]<char_m[j+1][1]:
            char_m[j],char_m[j+1]=char_m[j+1],char_m[j]
f = 0
for i in char_m:
    if (i[1]!=0):
        print i        
    f+=1
        
    
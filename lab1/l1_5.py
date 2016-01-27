# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


__author__ = "Aleks"
__date__ = "$26.01.2016 17:59:14$"
a = 0

if __name__ == "__main__":
    print "Hello World\n"
money = 0


i = 0
j = 0
mass = [];
while i<9:
    j = 0
    while j<9:
        if ((i+j)%7==0) and (i+j)>0:
            mass.append(str(i)+str(j))
        j=j+1
    i=i+1


print [str(k) for k in mass]



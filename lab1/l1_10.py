# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


__author__ = "Aleks"
__date__ = "$26.01.2016 17:59:14$"

li = [2,4,7,10,15,19,20,26]
n = 1
flag = 1
while n < len(li):
     for i in range(len(li)-n):
          if li[i] > li[i+1]:
               flag = 0
     n += 1
     
if flag==0:
    print "FALSE"
else:
    print "TRUE"

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

stroka = raw_input("Enter stroka=")
mass = []
i = 0
while i<255:
    mass.append(0)
    i+=1
    
i = 0
for k in stroka:
    mass[ord(k)] +=1 

    
i = 0
while i<255:
    if (mass[i]==1):
        print chr(i)
    i+=1
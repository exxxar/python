# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Aleks"
__date__ = "$26.01.2016 17:59:14$"
a = 0

if __name__ == "__main__":
    print "Hello World\n"
x = 0    
while True:
     try:
            x = int(raw_input("Enter N="))
            if x>0 and x<=100:
                break
            else:
                print "Must be in range 1..100"
     except ValueError:
            print "Bad Number"
    
if (x % 10 == 0 or (x > 10 and x<20) or (x>=5 and x<=9)):
    print str(x)+" let" 

    
if (x > 20 and ((x-1) % 10 == 0)) or x==1:
    print str(x)+" god" 

if (x > 20 and (
    ((x-2) % 10 == 0) or
    ((x-3) % 10 == 0) or
    ((x-4) % 10 == 0)
    )) or (x>=2 and x<=4):
    print str(x)+" goda" 

if x > 20 and (
    ((x-5) % 10 == 0) or
    ((x-6) % 10 == 0) or
    ((x-7) % 10 == 0) or
    ((x-8) % 10 == 0) or
    ((x-9) % 10 == 0)
    ):
    print str(x)+" let" 


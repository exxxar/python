# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

def format(x):
    x = str(x)
    if (len(x)<2):
        x = str(x+"0")
    return x

__author__ = "Aleks"
__date__ = "$26.01.2016 17:59:14$"
a = 0

if __name__ == "__main__":
    print "Hello World\n"
money = 0

real = 0
coins = 0

while True:
     try:
            money = float(raw_input("Enter money="))
            if money>=0:
                break
            else:
                print "Must be above then 0"
     except ValueError:
            print "Bad money sum"

if (str(money)).find(".")!=-1:
    money = (str(money)).split(".")
    real = money[0]
    coins = format(money[1])
else:
    real = money
    coins = "00"
print real+"p. "+coins+"kop."
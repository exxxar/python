# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

def format(x):
    x = str(x)
    if (len(x)<2):
        x = str("0"+x)
    return x

def format2(x):
    x = str(x)
    if (len(x)<4):
        x = str("0"+x)
        x = format2(x)
    return x

__author__ = "Aleks"
__date__ = "$26.01.2016 17:59:14$"
a = 0

if __name__ == "__main__":
    print "Hello World\n"
dd = 0
mm = 0
yy = 0
while True:
     try:
            dd = int(raw_input("Enter DD="))
            if dd>=1 and dd<=31:
                dd = format(dd)
                break
            else:
                print "Must be in range 1..31"
     except ValueError:
            print "Bad day"

while True:
     try:
            mm = int(raw_input("Enter MM="))
            if mm>=1 and mm<=12:
                mm = format(mm)
                break
            else:
                print "Must be in range 1..12"
     except ValueError:
            print "Bad month"

while True:
     try:
            yy = int(raw_input("Enter YY="))
            if yy>=1 and yy<=3000:
                yy = format2(yy)
                break
            else:
                print "Must be in range 1..3000"
     except ValueError:
            print "Bad month"
    
    

print dd+"\\"+mm+"\\"+yy

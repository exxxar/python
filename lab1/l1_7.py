__author__ = "Aleks"
__date__ = "$26.01.2016 17:59:14$"
p1 = ""
p2 = ""
p3 = ""
p4 = ""
x = 0;
while True:
     try:
            x = str(raw_input("Enter card number[16 numbers]="))
            if len(x)==16:
                break
            else:
                print "length must be 16 digets"
     except ValueError:
            print "Bad Number"

p1 = x[0:4:1]
p2 = x[4:8:1]
p3 = x[8:12:1]
p4 = x[12:16:1]
print "Chislo:"+p1+" **** ****"+p4


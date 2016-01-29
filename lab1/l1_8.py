    
__author__ = "Aleks"
__date__ = "$26.01.2016 17:59:14$"
predlojenie = ""
mass = []



while True:
     try:
            predlojenie = str(raw_input("Enter predlojenie="))
            if len(predlojenie)!=0:
                break
            else:
                print "length must not be null"
     except ValueError:
            print "Bad data"

mass = predlojenie.split(' ')
print [str(k) for k in mass]

n = 1 
while n < len(mass):
     for i in range(len(mass)-n):
          if len(mass[i]) < len(mass[i+1]):
               mass[i],mass[i+1] = mass[i+1],mass[i]
     n += 1
     
n = 0;

while n<len(mass):
        print mass[n]
        n+=1



 
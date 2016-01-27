# and open the template in the editor.
import random

def test1(x,k):    
    if k<x:
        if (k*2<x) or (abs(x-k)>abs(x-k*2)):
           k = k*2
        else:
            return k
        k = test1(x,k)
    return k

N = random.randint(1, 1000)
mass_N = random.sample(range(1000),N)
print mass_N
print "Mass length="+str(len(mass_N))
newLen = test1(len(mass_N),2)
print str(newLen)
mass_N2 = []
if (newLen<len(mass_N)):
    mass_N2 = mass_N[0:newLen:1]
else:
    mass_N2 = mass_N
    i = len(mass_N)
    while i<newLen:
        mass_N2.append(0)
        i+=1

print mass_N2


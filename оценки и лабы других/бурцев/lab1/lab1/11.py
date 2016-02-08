import math
N= int(raw_input('Input N'))
x=y=z=k=0
b=0.0
qN=int(math.pow(N,1.0/3))
for x in range(0,qN+2):
    for y in range(x,qN+2):
        for z in range(y,qN+2):
            
            b=math.pow(x,3)+math.pow(y,3)+math.pow(z,3)
            
            
            if(b==N):
                print "x = " + str(x) + "   y = " + str(y) + "  z = " + str(z)
                k+=1
if k==0:
    print 'no such combinations!'

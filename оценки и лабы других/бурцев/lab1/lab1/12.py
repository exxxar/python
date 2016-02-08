import math
print 'start'
arr= range(1,10000)
for N in arr:
    arrN=""
    x=y=z=k=0
    b=0.0
    qN=int(math.pow(N,1.0/3))
    for x in range(0,qN+2):
        for y in range(x,qN+2):
            for z in range(y,qN+2):
                
                b=math.pow(x,3)+math.pow(y,3)+math.pow(z,3)
                
                
                if(b==N):
                    
                    arrN+= "x = " + str(x) + "   y = " + str(y) + "  z = " + str(z)+"\n"
                    k+=1
    if(k>=3):
        print "N("+str(N)+"): "
        print arrN
    arrN=""
    k=0
print 'finish'


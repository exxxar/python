import math

N = 0
while True:
    try:
        N = int(raw_input("N="))
        if (N>0):
            break;
    except:
        print "Error number"
index = 3
sum = 0.0
while index<N:
    sum = float(sum) - float((1.0/index)+(1.0/(index+2)))
    print str(sum) + "["+str(index)+"]"
    index +=4
sum = 1 - sum
sum = 4 * sum
print "pi_1:" + str(sum) + " pi_2:"+str(math.pi)
raw_input()
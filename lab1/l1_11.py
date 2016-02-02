import math
N = 0
while True:
    try:
        N = int(raw_input("Enter numebr="))        
        if (N>=0):
            break
    except:
        print "Error value"
mas = []
flag = False
for i in range(100):
    for j in range(100):
        for k in range(100):
            sum = math.pow(i,3)+math.pow(j,3)+math.pow(k,3)
            if (sum==N):
                m = [i,j,k,sum]
                mas.append(m)
                flag = True
                

if (flag==False):
    print "Nothing to find"
else:
    for i in range(len(mas)):
        count = 0
        number = mas[i][3]
        for j in range(len(mas)):
            if (mas[j][3]==number):
                count+=1
        
        if (count>=3):
            print "["+str(number)+"]="+str(count)
            continue


            
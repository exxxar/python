import random
A = range(10,0,-1)
print A
print all(A[i-1]<A[i] for i in range(1, len(A)))
print "---------------"
A = range(0,10,1)
print A
print all(A[i-1]<A[i] for i in range(1, len(A)))
print "---------------"
A = [random.randrange(1, 100) for i in range(10)]
print A
print all(A[i-1]<A[i] for i in range(1, len(A)))

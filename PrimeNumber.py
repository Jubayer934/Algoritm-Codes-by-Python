import math
def isprime(x):
    if(a==1):
        return False
    for i in range(2,x+1):
        if (x%i==0):
            return False
        return True
a=int(input())
a=int(math.sqrt(a))
p=isprime(a)
print(p)
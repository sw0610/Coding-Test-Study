import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
    

n=int(input())

while True:
    if isPrime(n)==True:
        if str(n)==str(n)[::-1]:
            print(n)
            break
        else:
            n+=1
    else:
        n+=1

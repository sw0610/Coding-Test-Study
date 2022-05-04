import math
def isPrime(x):
    if x<2:
        return False
    
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            return False
        
    return True
        
    

n=int(input())

for i in range(n):
    x=int(input())
    while True:
        if isPrime(x)==True:
            print(x)
            break
        else:
            x+=1
    

            

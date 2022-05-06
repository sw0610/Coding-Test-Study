import math
import sys

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
        

n=int(sys.stdin.readline())
mlist=list(map(int, sys.stdin.readline().split()))
plist=set([])
for num in mlist:
    if isPrime(num)==True:
        plist.add(num)

if len(plist)==0:
    print(-1)
else:
    res=1
    for i in plist:
        res*=i//math.gcd(res, i)
    print(res)

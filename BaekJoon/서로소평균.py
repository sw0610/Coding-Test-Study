import sys
import math

n=int(sys.stdin.readline())
nums=list(map(int, sys.stdin.readline().split()))
x=int(sys.stdin.readline())

mlist=[]

for num in nums:
    if math.gcd(num, x)==1:
        mlist.append(num)
print(sum(mlist)/len(mlist))
        

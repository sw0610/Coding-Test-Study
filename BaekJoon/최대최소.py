import random

N=int(input())
mlist=[0 for i in range(N)]
mlist=list(map(int, input().split()))

print(min(mlist),end=" ")
print(max(mlist))

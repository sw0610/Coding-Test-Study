import sys
import heapq
n=int(input())
nums=[]

for i in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        if len(nums)==0:
            print(0)
        else:
            print(heapq.heappop(nums)[1])
    else:
        heapq.heappush(nums, (-x,x))
            

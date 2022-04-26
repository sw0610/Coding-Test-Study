'''
n=int(input())
mlist=list(map(int, input().split()))
indexs=[]
res=[]
for i in range(n):
    indexs.append(i+1)

idx=0
x=mlist.pop(idx)
res.append(indexs.pop(idx))

while mlist:
    if x<0:
        idx=(idx+x)%len(mlist)
    else:
        idx=(idx+(x-1))%len(mlist)

    x=mlist.pop(idx)
    res.append(indexs.pop(idx))

for i in res:
    print(i, end=" ")
'''

from collections import deque
n=int(input())
queue=deque(enumerate(map(int, input().split())))
res=[]

while queue:
    idx, num=queue.popleft()
    res.append(idx+1)
    if num>0:
        queue.rotate(-(num-1))
    elif num<0:
        queue.rotate(-num)
print(' '.join(map(str, res)))
            
    
        

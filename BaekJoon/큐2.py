import sys
from collections import deque

n=int(sys.stdin.readline())
queue=deque([])

for _ in range(n):
    order=sys.stdin.readline().split()
    w=order[0]

    if w=='push':
        queue.append(order[1])
    elif w=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif w=='size':
         print(len(queue))
    elif w=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif w=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif w=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
        
    
    

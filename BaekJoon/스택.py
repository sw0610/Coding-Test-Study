import sys

n=int(sys.stdin.readline())
mlist=[]

for i in range(n):
    x=sys.stdin.readline().split()
    w=x[0]
    if w=='push':
        mlist.append(x[1])
    elif w=='pop':
        if len(mlist)==0:
            print(-1)
        else:
            print(mlist.pop())
    elif w=='size':
        print(len(mlist))
    elif w=='empty':
        if len(mlist)==0:
            print(1)
        else:
            print(0)
    elif w=='top':
        if len(mlist)==0:
            print(-1)
        else:
            print(mlist[-1])
        
        
        

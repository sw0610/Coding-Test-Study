n, m=map(int, input().split())

lights=list(map(int,input().split()))

for i in range(m):
    
    mlist=list(map(int,input().split()))
    
    l=mlist[1]
    r=mlist[2]
    
    if mlist[0]==1:
         lights[l-1]=mlist[2]
         
    elif mlist[0]==2:
        for i in range(r-l+1):
            if lights[i+l-1]==0:
                lights[i+l-1]=1
            elif lights[i+l-1]==1:
                lights[i+l-1]=0
    elif mlist[0]==3:
        for i in range(r-l+1):
            lights[i+l-1]=0
    elif mlist[0]==4:
        for i in range(r-l+1):
            lights[i+l-1]=1

print(*lights,end=" ") 

T=int(input())
for i in range(1,T+1):
    N=int(input())
    mlist=list(map(int, input().split()))
    res=0
    x=mlist[len(mlist)-1]
    for j in range(len(mlist)-2,-1,-1):
        
        if mlist[j]<x:
            res+=x-mlist[j]
            
        elif mlist[j]>x:
            x=mlist[j]
            
    print("#%d %d"%(i,res))
        
    
        

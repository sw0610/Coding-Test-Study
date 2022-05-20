import sys
for i in range(1,11):
    n=int(input())
    mlist=list(map(int, sys.stdin.readline().split()))
    res=0
    for j in range(2,len(mlist)):
        if (mlist[j-2]<mlist[j]) and (mlist[j-1]<mlist[j]) and (mlist[j]>mlist[j+1]) and (mlist[j]>mlist[j+2]):
            res+=mlist[j]-max(mlist[j-2], mlist[j-1], mlist[j+1], mlist[j+2])
            j+=2
    print("#%d %d" %(i, res))
            
        
    

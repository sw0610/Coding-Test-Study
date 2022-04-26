x=int(input())


for i in range(x):
    n,m=map(int, input().split())
    plist=list(map(int, input().split()))
    idx=[0 for _ in range(n)]
    idx[m]=1

    cnt=0
    
    while True:
        if plist[0]==max(plist):
            cnt+=1
            if idx[0]==1:
                print(cnt)
                break
            else:
                plist.pop(0)
                idx.pop(0)
        else:
            plist.append(plist[0])
            idx.append(idx[0])
            plist.pop(0)
            idx.pop(0)
        
            

    

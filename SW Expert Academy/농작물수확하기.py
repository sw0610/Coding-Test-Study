T=int(input())
for i in range(1,T+1):
    n, k=map(int, input().split())
    mlist=[list(map(int, input().split())) for _ in range(n)]


    res=0
    for x in range(n):
        cnt=0
        for y in range(n):
            if mlist[x][y]==1:
                cnt+=1
            if mlist[x][y]==0 or y==n-1:
                if cnt==k:
                    res+=1
                cnt=0
                    
    for x in range(n):
        cnt=0
        for y in range(n):
            if mlist[y][x]==1:
                cnt+=1
            if mlist[y][x]==0 or x==n-1:
                if cnt==k:
                    res+=1
                cnt=0

    print(f"#{i} {res}")
                
    

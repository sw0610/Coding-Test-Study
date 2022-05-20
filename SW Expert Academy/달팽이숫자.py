T=int(input())

dx=[0,1,0,-1]
dy=[1,0,-1,0] #우하좌상

for i in range(1,T+1):
    n=int(input())
    dr=0
    a=0
    b=0
    num=1
    mlist=[[0]*n for _ in range(n)]

    while num<=n*n:
        for k in range(1,n*n+1):
            mlist[a][b]=num
            aa=a+dx[dr]
            bb=b+dy[dr]
            if aa not in range(n) or bb not in range(n) or mlist[aa][bb]!=0:
                dr=(dr+1)%4
            a=a+dx[dr]
            b=b+dy[dr]
            num+=1

    print(f"#{i}")
    for l in mlist:
        print(*l)
        
        

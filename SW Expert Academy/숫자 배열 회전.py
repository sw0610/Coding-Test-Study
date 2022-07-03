T=int(input())
for i in range(1, T+1):
    n=int(input())
    mlist=[list(map(int, input().split())) for _ in range(n)]
    m90=[[0 for _ in range(n)] for _ in range(n)]
    m180=[[0 for _ in range(n)] for _ in range(n)]
    m270=[[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(n):
            m90[j][k]=mlist[n-k-1][j]

    for j in range(n):
        for k in range(n):
            m180[j][k]=m90[n-k-1][j]
            
    for j in range(n):
        for k in range(n):
            m270[j][k]=m180[n-k-1][j]

    print(f"#{i}")
    for x in range(n):
        for y in range(n):
            print(m90[x][y], end='')
        print(end=' ')
        for q in range(n):
            print(m180[x][q], end='')
        print(end=' ')
        for w in range(n):
            print(m270[x][w end='')
        print()
            

n=int(input())

board=[]
for i in range(n):
    board.append(list(map(int, input())))

dx=[0,0,-1,1]
dy=[-1,1,0,0]


def dfs(x, y):
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if board[x][y]==1:
        global cnt
        board[x][y]=0
        cnt+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx, ny)
        return True
    return False
res=0
cnt=0
ans=[]
for i in range(n):
    for j in range(n):
        if dfs(i, j)==True:
            ans.append(cnt)
            res+=1
            cnt=0
ans.sort()
print(res)
for i in range(len(ans)):
    print(ans[i])

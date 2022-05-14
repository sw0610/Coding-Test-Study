n=int(input())
x=int(input())

mlist=[[0 for _ in range (n)] for _ in range (n)]

dx=[0,1,0,-1] #상우하좌
dy=[-1,-0,1,0]

a=n//2
b=n//2

num=1
slen=0

mlist[a][b]=num

while True:
    for i in range(4):
        for _ in range(slen):
            a+=dx[i]
            b+=dy[i]
            num+=1
            mlist[a][b]=num
            if num==x:
                res=[a+1, b+1]
    if a==b==0:
        break
    a-=1
    b-=1
    slen+=2

for i in range(n):
    print(*mlist[i])
print(*res)
            

n=int(input())
mlist=[-1]*10
cow=[]
cnt=0

for i in range(n):
    x, y=map(int, input().split())
    if x in cow:
        if mlist[x-1]!=y:
            cnt+=1
            mlist[x-1]=y
    else:
        cow.append(x)
        mlist[x-1]=y

print(cnt)

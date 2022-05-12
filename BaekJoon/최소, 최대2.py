t=int(input())
for i in range(t):
    n=int(input())
    mlist=list(map(int, input().split()))
    print(min(mlist), max(mlist),end=" ")

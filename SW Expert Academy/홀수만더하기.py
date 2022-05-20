import sys

T=int(sys.stdin.readline())

for i in range(T):
    case=list(map(int, sys.stdin.readline().split()))
    res=[]
    for c in case:
        if c%2==1:
            res.append(c)
    print("#%d %d"%(i+1,sum(res)))

from itertools import combinations

T=int(input())
for tc in range(1, T+1):
    n=int(input())

    mlist=[]
    for i in range(n):
        x, y=input().split()
        for j in range(int(y)):
            mlist.append(x)

    print(f"#{tc}")
    for k in range(len(mlist)):
        print(mlist[k], end='')
        if k%10==9:
            print()
    print()
        

    

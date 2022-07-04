def check(mlist):
    ans=1
    for i in range(9):
        if len(set(mlist[i]))==9:
            ans=1
        else:
            return 0
    for i in range(9):
        klist=[]
        for j in range(9):
            klist.append(mlist[j][i])
        if len(set(klist))==9:
            ans=1
        else:
            return 0

    for i in range(0, 7, 3):
        for x in range(0, 7, 3):
            klist=[]
            for j in range(3):
                for k in range(3):
                    klist.append(mlist[j+i][k+x])
            if len(set(klist))==9:
                ans=1
            else:
                return 0
    return 1

t=int(input())

for tc in range(1, t+1):
    mlist=[]
    
    for i in range(9):
        mlist.append(list(map(int, input().split())))
    
    print(f"#{tc} {check(mlist)}")

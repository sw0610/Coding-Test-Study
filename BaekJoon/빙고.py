import sys

def isBingo(arr):
    cnt=0
    for l in arr:
        if l.count(0)==5:
            cnt+=1
    for i in range(5):
        y=0
        for j in range(5):
            if arr[j][i]==0:
                y+=1
        if y==5:
            cnt+=1
    k=0
    for i in range(5):
        if arr[i][i]==0:
            k+=1
    if k==5:
        cnt+=1
    u=0
    for i in range(5):
        if arr[i][4-i]==0:
            u+=1
    if u==5:
        cnt+=1
    return cnt

bingo=[]
for i in range(5):
    bingo.append(list(map(int, sys.stdin.readline().split())))
    

cal=[]
for i in range(5):
    cal+=list(map(int, sys.stdin.readline().split()))
   
for c in cal:
    for b in bingo:
        if c in b:
            b[b.index(c)]=0

            break
        else:
            continue

    res=isBingo(bingo)
    if res>=3:
        print(cal.index(c)+1)
        break

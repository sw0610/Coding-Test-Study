n=int(input())
mlist=[]

for _ in range(n):
    w, h=map(int, input().split())
    mlist.append((w ,h))

for i in mlist:
    r=1
    for j in mlist:
        if i[0]<j[0] and i[1]<j[1]:
            r+=1
    print(r, end=" ")
    

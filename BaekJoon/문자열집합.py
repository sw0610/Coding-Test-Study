import sys
n, m=map(int, sys.stdin.readline().split())

mlist=dict()


for i in range(n):
    s=sys.stdin.readline().strip()
    mlist[s]=True
    
cnt=0
for _ in range(m):
    word=sys.stdin.readline().strip()
    if word in mlist.keys():
        cnt+=1
print(cnt)

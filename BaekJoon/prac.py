import sys
n=int(sys.stdin.readline())
mlist=[]
num=0
for i in range(n+1):
    if i==0:
        num=0
    elif i==1:
        num=1
    else:
        num=mlist[-2]+mlist[-1]
    
    mlist.append(num)

print(mlist[-1])

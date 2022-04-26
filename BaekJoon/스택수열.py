n=int(input())
nums=[]
res=[]
pos=True
cnt=0

for i in range(n):
    x=int(input())

    while cnt<x:
        cnt+=1
        nums.append(cnt)
        res.append('+')

    if nums[-1]==x:
        nums.pop()
        res.append("-")
    else:
        pos=False

if pos==False:
    print("NO")
else:
    print("\n".join(res))

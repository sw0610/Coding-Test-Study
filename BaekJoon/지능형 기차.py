sum=0
mlist=[]

for i in range(0,10):
  x,y=map(int, input().split())
  sum=sum-x+y
  mlist.append(sum)

print(max(mlist))

N, K=map(int, input().split())
x=[]

for i in range (1,N+1):
    if N%i==0:
       x.append(i)

if len(x)>=K:
  print(x[K-1])
else:
  print(0)

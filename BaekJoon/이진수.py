T=int(input())

for i in range(0, T):
  n=int(input())
  cnt=0
  while n>0:
    if(n%2==1):
      print(cnt, end=" ")
    cnt+=1
    n=n//2

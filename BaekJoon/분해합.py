n=int(input())

for i in range(1, n+1):
    x=list(map(int, str(i)))
    s=i+sum(x)
    if s==n:
        print(i)
        break
else:
    print(0)

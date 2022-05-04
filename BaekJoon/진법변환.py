n, b=input().split()

n=n[::-1]
b=int(b)

nums='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

res=0

for i in range(len(n)):
    res+=nums.index(n[i])*(b**i)

print(res)



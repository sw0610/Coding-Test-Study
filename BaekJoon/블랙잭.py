n, m=map(int, input().split())
num=list(map(int, input().split()))
res=0

for i in range(0, len(num)-2):
    for j in range(i+1, len(num)-1):
        for k in range(j+1, len(num)):
            s=num[i]+num[j]+num[k]
            if s>m:
                continue
            else:
                res=max(res, s)
print(res)
            

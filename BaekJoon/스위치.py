n=int(input())
switch=list(map(int, input().split()))
k=int(input())
for i in range(k):
    a, b=map(int, input().split())
    if a==1:
        for i in range(n):
            if (i+1)%b==0:
                if switch[i]==0:
                    switch[i]=1
                elif switch[i]==1:
                    switch[i]=0
            else:
                continue
            
    elif a==2:
        if switch[b-1]==0:
           switch[b-1]=1
        elif switch[b-1]==1:
            switch[b-1]=0
        
        i=1
        while b-1-i>=0 and b+i<=n:
            if switch[b-1-i]==switch[b-1+i]:
                if  switch[b-1-i]==0:
                    switch[b-1-i]=1
                    switch[b-1+i]=1
                elif switch[b-1-i]==1:
                    switch[b-1-i]=0
                    switch[b-1+i]=0
                
                i+=1
                
                
            else:
                break

for i in range(0, n, 20):
    print(*switch[i:i+20])

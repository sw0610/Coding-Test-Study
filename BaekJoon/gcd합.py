from itertools import combinations
def gcd(a,b):
    while b>0:
        a, b=b, a%b
    return a

t=int(input())
for i in range(t):
    res=0
    n, *mlist=map(int, input().split())
    cblist=list(combinations(mlist, 2))

    for k in cblist:
        res+=gcd(k[0], k[1])
                
    print(res)
        
    
        

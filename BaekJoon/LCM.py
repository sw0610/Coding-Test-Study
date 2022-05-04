def myGdc(a, b):
    while b>0:
        a, b=b, a%b
    return a
        
n=int(input())

for i in range(n):
    a, b=map(int, input().split())
    x=myGdc(a, b)
    print((a*b)//x)
    

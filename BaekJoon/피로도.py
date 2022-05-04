a,b,c,m=map(int, input().split())

time=0
f=0
work=0

if a>m:
    print(0)
else:
    while time<24:
        time+=1
        if f+a<=m:
            f+=a
            work+=b
        else:
            if f-c>=0:
                f-=c
            else:
                f=0
    print(work)
    

                
            
            
            
    





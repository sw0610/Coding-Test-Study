n=int(input())

for i in range(n):
    x=input()
    cnt=0
    for j in x:
        if j=="(":
            cnt+=1
        elif j==")":
            cnt-=1
        if cnt<0:
            print("no")
            break
    if cnt==0:
        print("yes")
    elif cnt>0:
        print("no")
            

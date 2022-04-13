n=int(input())

mlist=list(str(n))
cnt=[0]*10

for i in range(len(mlist)):
    num=int(mlist[i])
    if num==6 or num==9:
        cnt[6]+=1
    else:
        cnt[num]+=1
if cnt[6]%2==0:
    cnt[6]=cnt[6]//2
else:
    cnt[6]=cnt[6]//2+1

print(max(cnt))
    
    

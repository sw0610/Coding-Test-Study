n,k=map(int, input().split())
mlist=[i for i in range(2, n+1)]
nums=[]

while len(mlist)!=0:
    p=min(mlist)
    nums.append(p)
    mlist.remove(p)
    
    for m in mlist:
        if m%p==0:
            nums.append(m)
            mlist.remove(m)

print(nums[k-1])
        

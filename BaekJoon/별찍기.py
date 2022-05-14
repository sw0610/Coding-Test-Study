def myStar(n ,idx):
    length=4*n-3

    if n==1:
        mlist[idx][idx]='*'
        return
    
    for i in range(idx, length+idx):
        mlist[idx][i]='*'
        mlist[i][idx]='*' 
        mlist[idx+length-1][i]='*'
        mlist[i][idx+length-1]='*'

    return myStar(n-1, idx+2)

n=int(input())
lens=4*n-3
mlist=[[' ']*lens for _ in range(lens)]

myStar(n, 0)

for i in mlist:
    print(''.join(i))    
        
    




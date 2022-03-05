def solution(dartResult):
    answer = 0
    n=''
    mlist=[]
    
    for i in dartResult:
        if i.isnumeric():
            n+=i
        elif i=='S':
            mlist.append(int(n)**1)
            n=''
        elif i=='D':
            mlist.append(int(n)**2)
            n=''
        elif i=='T':
            mlist.append(int(n)**3)
            n=''
            
        elif i=='*':
            if len(mlist)>1:
                mlist[-1]*=2
                mlist[-2]*=2
            else:
                mlist[-1]*=2
        elif i=='#':
            mlist[-1]=mlist[-1]*-1
    
    answer=sum(mlist)
    
    return answer

s=input()

mlist=""
mystr=""
tag=False
for i in range(len(s)):
    
    if s[i]==' ':
        mystr+=mlist[::-1]+" "
        mlist=""
        continue
        
    elif s[i]=='<':
        tag=True
        mystr+=mlist[::-1]
        mlist=""
        mystr+=s[i]
        continue
    
    elif s[i]=='>':
        tag=False
        mystr+=mlist+">"
        continue
        

    if tag:
        mystr+=s[i]
    else:
        mlist+=s[i]

print(mystr+mlist[::-1])
        

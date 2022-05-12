n=input()
mlist=[]
i=0

while i<len(n):
    if n[i:i+4]=="XXXX":
        mlist.append("AAAA")
        i+=4
    elif n[i:i+2]=="XX":
        mlist.append("BB")
        i+=2
    elif n[i]==".":
        mlist.append(".")
        i+=1
    else:
        break

res="".join(mlist)
if len(res)==len(n):
    print(res)
else:
    print(-1)
    

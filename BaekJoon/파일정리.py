n=int(input())

mydict=dict([])

for i in range(n):
    file=input().split('.')[1]
    if file not in mydict:
        mydict[file]=1
    else:
        mydict[file]+=1
        
for k, v in sorted(mydict.items()):
    print(k, v)


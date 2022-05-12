import sys
mlist=[]
for i in range(28):
    mlist.append(int(sys.stdin.readline()))

nlist=[]
for i in range(1,31):
    if i not in mlist:
        nlist.append(i)
    else:
        continue

print(min(nlist))
print(max(nlist))
        
                 

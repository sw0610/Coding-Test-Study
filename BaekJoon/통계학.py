from collections import Counter
import sys

n=int(input())
mlist=[]

for _ in range(n):
    mlist.append(int(sys.stdin.readline()))


print(round(sum(mlist)/n))

mlist.sort()
print(mlist[n//2])

cnt=Counter(mlist).most_common(2)
if n>1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(max(mlist)-min(mlist))
    

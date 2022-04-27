import sys

n, m=map(int, sys.stdin.readline().split())
poket={}

for i in range(1,n+1):
    name=sys.stdin.readline().strip()
    poket[i]=name
    poket[name]=i
    
for _ in range(m):
    quest=sys.stdin.readline().strip()
    if quest.isalpha():
        print(poket[quest])
    else:
        print(poket[int(quest)])


        

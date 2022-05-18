import sys

board=[]
for i in range(19):
    board.append(list(map(int, sys.stdin.readline().split())))

dx=[0,1,1,-1] 
dy=[1,0,1,1]
for i in range(19):
    for i in range(19):
        

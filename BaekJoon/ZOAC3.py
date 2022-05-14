sl, sr=input().split()
word=input()

board=['qwertyuiop','asdfghjkl','zxcvbnm']
leftk="qwertasdfgzxcv"


res=0

for i in range(len(board)):
    if sl in board[i]:
        lx=i
        ly=board[i].index(sl)
    if sr in board[i]:
        rx=i
        ry=board[i].index(sr)

for w in word:
    res+=1

    if w in leftk:
        for i in range(len(board)):
            if w in board[i]:
                la=i
                lb=board[i].index(w)

                res+=abs(lx-la)+abs(ly-lb)

                lx=la
                ly=lb

                break
    else:
        for i in range(len(board)):
            if w in board[i]:
                ra=i
                rb=board[i].index(w)

                res+=abs(rx-ra)+abs(ry-rb)

                rx=ra
                ry=rb

                break

print(res)
        
        
        
            
    

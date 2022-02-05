def solution(board, moves):
    answer = 0
    myStack = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                myStack.append(board[i][move - 1])
                board[i][move - 1] = 0

                if len(myStack) > 1:
                    if myStack[-1] == myStack[-2]:
                        myStack.pop(-1)
                        myStack.pop(-1)
                        answer += 2
                break

    return answer
def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        mlist = array[commands[i][0] - 1:commands[i][1]]
        mlist.sort()
        answer.append(mlist[commands[i][2] - 1])

    return answer
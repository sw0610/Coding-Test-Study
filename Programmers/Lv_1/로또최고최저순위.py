def solution(lottos, win_nums):
    cnt = 0
    score = 0
    answer = []
    zeros = lottos.count(0)

    for l in lottos:
        if l != 0 and l in win_nums:
            cnt += 1

    answer.append(7 - (cnt + zeros))
    answer.append(7 - cnt)

    if zeros == 6:
        answer = [1, 6]
    elif zeros == 0 and cnt == 0:
        answer = [6, 6]

    return answer
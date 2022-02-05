def solution(d, budget):
    answer = 0
    d.sort()
    s = 0

    for i in d:
        s += i
        if s > budget:
            break
        else:
            answer += 1

    return answer
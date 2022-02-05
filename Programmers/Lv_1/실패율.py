def solution(N, stages):
    answer = []
    rate = {}
    s = len(stages)
    for i in range(1, N + 1):
        if s == 0:
            rate[i] = 0
        else:
            cnt = stages.count(i)
            rate[i] = cnt / s
            s -= cnt

        answer = sorted(rate, key=lambda x: rate[x], reverse=True)
    return answer
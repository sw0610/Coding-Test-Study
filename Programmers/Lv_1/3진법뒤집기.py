def solution(n):
    answer = 0
    s = ''
    while n > 0:
        r = n % 3
        n = n // 3
        s += str(r)

    return int(s, 3)
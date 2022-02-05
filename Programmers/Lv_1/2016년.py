def solution(a, b):
    answer = ''

    x = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    s = -1

    for i in range(a - 1):
        s += x[i]
    s += b
    s = s % 7
    answer = d[s]
    return answer
def solution(numbers):
    answer = []

    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            s = numbers[i] + numbers[j]
            if s not in answer:
                answer.append(s)
    answer.sort()
    return answer
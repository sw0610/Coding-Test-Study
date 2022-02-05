def solution(nums):
    answer = 0
    n = len(nums) / 2

    nums = set(nums)

    if len(nums) < n:
        answer = len(nums)
    else:
        answer = n

    return answer
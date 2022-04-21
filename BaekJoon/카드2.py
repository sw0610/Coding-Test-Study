from collections import deque

n=int(input())
nums=deque([i for i in range(1,n+1)])

while len(nums)>1:
    nums.popleft()
    nums.append(nums[0])
    nums.popleft()

print(nums.pop())
    

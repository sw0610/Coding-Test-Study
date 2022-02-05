def solution(nums):
    answer=0

    for i in  range (0, len(nums)-2):
        for j in range (i+1, len(nums)-1):
            for k in range (j+1, len(nums)):
                    s=nums[i]+nums[j]+nums[k]
                    isS=True
                    for x in range(2, s):
                        if s%x==0:
                            isS=False
                            break

                    if isS==True:
                        answer+=1
    return answer

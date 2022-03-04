def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        
        a=bin(arr1[i]|arr2[i])[2:]
    
        a=a.zfill(n)
        a=a.replace('1','#')
        a=a.replace('0',' ')
        
        answer.append(a)

    return answer

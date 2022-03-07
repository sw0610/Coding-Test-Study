def solution(n, m):
    
    m1=max(n, m)
    n1=min(n, m)
    
    while n1:
        m1, n1 = n1, m1%n1
            
    
    return [m1, int(n * m / m1)]

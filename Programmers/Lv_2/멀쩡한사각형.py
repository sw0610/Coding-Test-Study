def solution(w,h):
    
    m1=max(w, h)
    n1=min(w, h)
    
    while n1:
        m1, n1=n1, m1%n1
    
    return w*h-(w+h-m1)

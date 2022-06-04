T=int(input())
month=['01','02','03','04','05','06','07','08','09','10','11','12']
m31=['01','03','05','07','08','10','12']
m30=['04','06','09','11']

for i in range(1, T+1):
    x=input()
    
    if x[4:6] not in month:
            print(f"#{i} -1")
            
        
    elif x[4:6]=="02":
        if x[6:]=='00' or int(x[6:])>28:
            print(f"#{i} -1")
            
        else:
            print(f"#{i} {x[0:4]}/{x[4:6]}/{x[6:]}")
                
    elif x[4:6] in m31:
        if x[6:]=='00' or int(x[6:])>31:
            print(f"#{i} -1")
            
        else:
            print(f"#{i} {x[0:4]}/{x[4:6]}/{x[6:]}")
        
    elif x[4:6] in m30:
        if x[6:]=='00' or int(x[6:])>30:
            print(f"#{i} -1")
            
        else:
            print(f"#{i} {x[0:4]}/{x[4:6]}/{x[6:]}")
        

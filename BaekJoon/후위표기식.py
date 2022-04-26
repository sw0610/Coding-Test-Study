n=int(input())
res=list(input())
nums=[]

for i in range(n):
    nums.append(int(input()))

stack=[]

for i in range(len(res)):
    if 'A'<=res[i]<='Z':
        stack.append(nums[ord(res[i])-ord('A')])
    else:
        x2=stack.pop()
        x1=stack.pop()

        if res[i]=='+':
            stack.append(x1+x2)
        elif res[i]=='-':
            stack.append(x1-x2)
        elif res[i]=='*':
            stack.append(x1*x2)
        elif res[i]=='/':
            stack.append(x1/x2)

print("%.2f" %stack[0])


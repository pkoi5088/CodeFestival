S=list(input())
stack=[]
flag=False
for i in S:
    if i=='(' or i=='{' or i=='[':
        stack.append(i)
    elif i==')':
        if len(stack)==0 or stack[len(stack)-1]!='(':
            flag=True
            break
        else:
            stack.pop()
    elif i=='}':
        if len(stack)==0 or stack[len(stack)-1]!='{':
            flag=True
            break
        else:
            stack.pop()
    elif i==']':
        if len(stack)==0 or stack[len(stack)-1]!='[':
            flag=True
            break
        else:
            stack.pop()

if flag:
    print("NO")
else:
    print("YES")
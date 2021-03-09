weight=int(input())
result=0
result+=weight//7
weight%=7
if weight%3==0:
    result+=weight//3
else:
    result=-1
print(result)
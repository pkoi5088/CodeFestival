a=[1,2,3,4]
b=['a','b','c','d']
result=[]

for i in range(len(a)):
    if i%2==0:
        result.append([a[i],b[i]])
    else:
        result.append([b[i],a[i]])
print(result)
name=list(input().split())
dish=list(map(int,input().split()))
result={}

for i in range(len(dish)):
    name[i]=(name[i],dish[i])

name.sort(key=lambda x:x[1],reverse=True)

for i in range(len(name)):
    result[name[i][0]]=i+1
print(result)
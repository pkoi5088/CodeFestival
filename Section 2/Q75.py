n=list(input())
result=0
cnt=1

for idx in range(len(n)-1,-1,-1):
    result+=int(n[idx])//3*cnt
    cnt*=3
print(result)
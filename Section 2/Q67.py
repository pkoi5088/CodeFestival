n=int(input())
result=[]

people=1
while(people*(people-1)//2<=n):
    people+=1
people-=1
result.append(n-people*(people-1)//2)
result.append(people+1)
print(result)
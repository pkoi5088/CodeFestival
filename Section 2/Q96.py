field=[]
field.append(list(input().split()))
for i in range(len(field[0])-1):
    field.append(list(input().split()))
N=len(field)
dp=[[0]*N for _ in range(N)]
loc=(0,0)
result=-1
for i in range(N):
    for j in range(N):
        if field[i][j]=='0':
            if i==0 or j==0 or field[i-1][j]=='1' or field[i][j-1]=='1':
                dp[i][j]=1
            else:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
            if result<dp[i][j]:
                result=dp[i][j]
                loc=(i,j)

for i in range(result):
    for j in range(result):
        field[loc[0]-i][loc[1]-j]='#'

print('{} X {}\n'.format(result,result))
for i in range(N):
    for j in range(N):
        print(field[i][j],end=' ')
    print('')
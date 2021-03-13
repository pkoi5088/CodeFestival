def solve():
    a,b=map(int,input().split())
    board=[[0 for _ in range(a)]for _ in range(a)]
    result=-1
    for i in range(a):
        board[i] = list(map(int,input().split()))

    for i in range(a-b+1):
        for j in range(a-b+1):
            sum=0
            for x in range(i,i+b):
                for y in range(j,j+b):
                    if board[x][y]:
                        sum+=1
            result=max(result,sum)
    return result

T=int(input())
while(T):
    print(solve())
    T-=1
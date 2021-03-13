graph=[[] for _ in range(5)]
dx=[(-1,0),(1,0),(0,-1),(0,1)]

for i in range(5):
    graph[i]=list(map(int,input().split()))

for i in range(5):
    for j in range(5):
        if graph[i][j]==1:
            print('f',end=' ')
        else:
            flag=False
            for l in range(4):
                nx=i+dx[l][0]
                ny=j+dx[l][1]
                if(nx>=0 and nx<5 and ny>=0 and ny<5):
                    if graph[nx][ny]==1:
                        flag=True
            if flag:
                print('*',end=' ')
            else:
                print('0',end=' ')
    print('')
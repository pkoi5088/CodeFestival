n=int(input('가로 = '))
m=int(input('세로 = '))
loc=list(map(int,input('캐릭터위치 = ').split()))
obj=list(map(int,input('장애물 = ').split()))
dir=[(-1,0),(1,0),(0,-1),(0,1)]

def make_map():
    board=[[0 for _ in range(n+2)] for _ in range(m+2)]
    for i in range(n+2):
        board[0][i]=2
        board[m+1][i]=2
    for i in range(m+2):
        board[i][0]=2
        board[i][n+1]=2
    board[loc[0]+1][loc[1]+1]=1
    for i in range(0,len(obj),2):
        board[obj[i]+1][obj[i+1]+1]=2
    for i in range(len(board)):
        print(board[i])
    return board
    
def move(board,inMove):
    for i in inMove:
        nx=loc[0]+1+dir[i-1][0]
        ny=loc[1]+1+dir[i-1][1]
        if board[nx][ny]==0:
            board[loc[0]+1][loc[1]+1]=0
            board[nx][ny]=1
            loc[0]=nx-1
            loc[1]=ny-1
    for i in range(len(board)):
        print(board[i])
    return board
        
print('캐릭터 이동 전 지도')
B=make_map()
command=list(map(int,input('움직임 = ').split()))
after=move(B,command)
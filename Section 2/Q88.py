n=int(input('가로 = '))
m=int(input('세로 = '))
loc=list(map(int,input('캐릭터위치 = ').split()))
obj=list(map(int,input('장애물 = ').split()))

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

make_map()    
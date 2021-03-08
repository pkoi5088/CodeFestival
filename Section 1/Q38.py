board=list(map(int,input().split()))
board.sort()
length=len(board)
cnt=0
differ=0
i=length-1
while i>=0 and differ<3:
    differ+=1
    cnt+=1
    while i>=0 and board[i]==board[i-1]:
        i-=1
        cnt+=1
    i-=1
print(cnt)
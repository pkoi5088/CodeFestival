n=int(input())
board=[]
while n!=0:
    board.append(str(n%2))
    n=n//2
board.reverse()
print(''.join(board))
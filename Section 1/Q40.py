limit=int(input())
n=int(input())
board=[]
for i in range(n):
    board.append(int(input()))
for i in range(len(board)):
    if sum(board[:i+1])>=limit:
        print(i)
        break
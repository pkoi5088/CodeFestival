N,K=map(int,input().split())
table=[i for i in range(1,N+1)]
idx=0
while len(table)>2:
    table.pop(idx)
    idx-=1
    N-=1
    idx=(idx+3)%N
print(table)
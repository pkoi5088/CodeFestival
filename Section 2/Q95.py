def rotate(stamp):
    N=len(stamp)
    ret=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret[j][N-i-1]=stamp[i][j]
    return ret

def solution(stamp,r):    
    N=len(stamp)
    ret=stamp
    tmp=stamp
    while r:
        tmp=rotate(tmp)
        for i in range(N):
            for j in range(N):
                ret[i][j]+=tmp[i][j]
        r-=1
    return ret

도장 = [
[1,1,1,2],
[2,0,0,0],
[1,1,1,1],
[0,0,0,0]
]

회전 = 1
print(solution(도장,회전))
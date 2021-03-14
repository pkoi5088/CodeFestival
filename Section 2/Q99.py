def solution(stone,rabbit):
    ret=[]
    for r in rabbit:
        now=r-1
        while now<len(stone) and stone[now]!=0:
            stone[now]-=1
            now+=r
        if now>=len(stone):
            ret.append('pass')
        else:
            ret.append('fail')
    return ret

돌의내구도=[1,2,1,4,5,2]
토끼의점프력=[2,1,3,1]
print(solution(돌의내구도,토끼의점프력))
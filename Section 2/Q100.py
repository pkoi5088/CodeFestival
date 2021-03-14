def solution(game,command):
    ret=0
    stack=[]
    for i in command:
        idx=0
        while idx<len(game) and game[idx][i-1]==0:
            idx+=1
        if idx==len(game):
            ret-=1
        else:
            if len(stack)==0 or stack[-1]!=game[idx][i-1]:
                stack.append(game[idx][i-1])
            else:
                ret+=game[idx][i-1]*2
                stack.pop()
            game[idx][i-1]=0
    return ret


퍼즐판 = [[0,0,0,0],[0,1,0,3],[2,5,0,1],[2,4,4,1],[5,1,1,1]]
조작 = [1,1,1,1,3,3,3]
print(solution(퍼즐판,조작))
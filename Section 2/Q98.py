def solution(s):
    numbers=[]
    sList=s.split(' ')
    for idx in range(1,len(sList),2):
        if ',' in sList[idx]:
            tmp=sList[idx].split(',')
            numbers+=tmp
        else:
            numbers.append(sList[idx])
    ret=[]
    for i in numbers:
        if int(i) not in ret:
            ret.append(int(i))
    return ret

print(solution("1번: 4,2,3 2번: 3 3번: 2,3,4,1 4번: 2,3"))
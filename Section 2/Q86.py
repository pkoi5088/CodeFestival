point=list(map(int,input().split()))
dish=int(input())
sequence=sorted(point)
count=0

for i in range(len(point)):
    point[i] = (i+1,point[i])

for goal in sequence:
    while point[0][1]!=goal:
        point.append(point.pop(0))
        count+=1
    if point[0][0]==dish:
        break
    point.pop(0)
    count+=1
print(count)
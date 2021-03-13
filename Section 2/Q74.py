graph = {
    1: [2, 3, 4],
    2: [1, 3, 4, 5, 6],
    3: [1, 2, 7],
    4: [1, 2, 5, 6],
    5: [2, 4, 6, 7],
    6: [2, 4, 5, 7],
    7: [3, 5, 6]
}

start,goal=map(int,input().split())
visit=[start]
result=0

def pick(n):
    global result
    if n==goal:
        result=max(result,len(visit))
    else:
        for i in graph[n]:
            if i not in visit:
                visit.append(i)
                pick(i)
                visit.pop()

pick(start)
print(result-1)
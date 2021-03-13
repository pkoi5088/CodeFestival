graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

start,goal=input().split()
queue=[]
visit=[]

def getDist():
    queue.append([start,0])
    visit.append(start)

    while len(queue)!=0:
        now=queue[0][0]
        dist=queue[0][1]
        queue.pop(0)
        if now==goal:
            return dist
        for i in graph[now]:
            if i not in visit:
                queue.append([i,dist+1])
                visit.append(i)

print(getDist())
page=list(input())
frame=int(input())
result=0
queue=[]

for i in page:
    if i in queue:
        result+=1
        idx=queue.index(i)
        queue.append(queue.pop(idx))
    else:
        result+=6
        if len(queue)==frame and len(queue)!=0:
            queue.pop(0)
        queue.append(i)
print(result)
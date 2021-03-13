N=int(input())-1
now='1'

while N:
    tmp=''
    visit=[]
    count=[]
    for i in now:
        if i not in visit:
            visit.append(i)
            count.append((int(i),str(now.count(i))))
    count.sort()
    for i in count:
        tmp+=str(i[0])
        tmp+=i[1]
    now=tmp
    N-=1
print(now)
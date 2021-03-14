def solution(n,l):
    ret=0
    delivery=[]
    while len(l)!=0:
        while len(l)!=0 and len(delivery)!=n:
            delivery.append(l.pop(0))

        m=min(delivery)
        ret+=m
        while m in delivery:
            delivery.pop(delivery.index(m))
        for idx in range(len(delivery)):
            delivery[idx]-=m
        
    while len(delivery)!=0:
        m=min(delivery)
        ret+=m
        while m in delivery:
            delivery.pop(delivery.index(m))
        for idx in range(len(delivery)):
            delivery[idx]-=m
    return ret
    

배달원=3
배달시간=[1,2,1,3,3,3]

print(solution(배달원,배달시간))
import random  as r

total_score = []
classAvg=[]
classTop=[]

#한 반에 30명 한 학년에 7반

for c in range(7):
    class_score = []
    for s in range(30):
        score = []
        for i in range(5):
            score.append(r.randint(1, 100))
        class_score.append(score)
    classTop.append(max(class_score))
    total_score.append(class_score)

for c in total_score:
    tmp=0
    for s in c:
        tmp += sum(s)/5
    classAvg.append(tmp // 30)

print(total_score)
print(classAvg)
print(classTop)
print(sum(classAvg)//7)
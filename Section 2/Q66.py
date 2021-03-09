탑 = ['ABCDEF', 'BCAD', 'ADEFQRX', 'BEDFG']
규칙 = 'ABD'
result=[]

for top in 탑:
    rule=0
    flag=True
    for c in top:
        if c in 규칙:
            if rule>규칙.index(c):
                result.append('불가능')
                flag=False
                break
            rule=규칙.index(c)
    if flag:
        result.append('가능')
print(result)
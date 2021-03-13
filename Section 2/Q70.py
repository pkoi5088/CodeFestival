a=([1,2],[2,4])
b=([1,0],[0,3])
result=[]

if(len(a[0])==len(b)):
    for i in range(len(a)):
        t=[]
        for j in range(len(a)):
            tmp=0
            for k in range(len(a[0])):
                tmp+=a[i][k]*b[k][j]
            t.append(tmp)
        result.append(t)
    print(result)
else:
    print('곱할 수 없습니다.')
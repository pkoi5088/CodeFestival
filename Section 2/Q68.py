busList=["12:30","13:20","14:13"]
time="12:40"
result=[]
tmp=time.split(':')
timeMinute=int(tmp[0])*60+int(tmp[1])

for i in busList:
    tmp=i.split(':')
    busMinute=int(tmp[0])*60+int(tmp[1])
    if(busMinute<timeMinute):
        result.append('지나갔습니다')
    else:
        result.append('{}시간 {}분'.format((busMinute-timeMinute)//60,(busMinute-timeMinute)%60))

print(result)
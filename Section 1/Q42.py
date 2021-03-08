days={1:31,2:29,3:31,4:30,5:31,6:31,7:31,8:31,9:30,10:31,11:30,12:31}
week={0:'WED',1:'THU',2:'FRI',3:'SAT',4:'SUN',5:'MON',6:'TUE'}

all=0
a,b=map(int,input().split())
for i in range(1,a):
    all+=days[i]
all+=b-1
print(week[all%7])
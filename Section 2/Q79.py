l = [10, 20, 25, 27, 34, 35, 39] #기존 입력 값
n = int(input('순회 횟수는 :'))

def rotate(inL, inN):
    tmp=-1
    result=(0,0)
    for idx in range(len(inL)):
        i=idx-inN
        if tmp==-1 or tmp>abs(l[idx]-l[i]):
            tmp=abs(l[idx]-l[i])
            result=(idx,i)
    print("index : {}".format(result[0]))
    print("value : {}, {}".format(l[result[0]],l[result[1]]))

rotate(l, n)
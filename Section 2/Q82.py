def math(e):
    stack=[]
    for i in e:
        if i=='(':
            stack.append(i)
        elif i==')':
            if len(stack)==0:
                return False
            stack.pop()
    return True

while 1:
    order = input('데이터 입력(1), 프로그램 종료(2) :')
    if order == '1':
        ex = input('데이터를 입력하세요 :')
        print(math(ex))
    else:
        break
import csv

f = open('test.csv', 'r', encoding='utf-8')
r = csv.reader(f)
for line in r:
    s1=[]
    s2=[]
    for i in line[1].replace(',', ''):
        print(i)
        if i == '3':
            s1.append('1')
            s2.append('2')
        elif i == '4':
            s1.append('2')
            s2.append('2')
        elif i == '6':
            s1.append('1')
            s2.append('5')
        else:
            s1.append(i)
            s2.append('0')
    print(int(''.join(s1)), int(''.join(s2)))
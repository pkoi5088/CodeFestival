import random as r

l = [chr(i) for i in range(65, 91)]

total_medicine = []
medicine = []

for i in range(100):
    total_medicine.append(r.sample(l, 8))
    
user = list(input().split(''))
result = []

for i in total_medicine:
    if len(set(i) & set(user[0]))==int(user[1]):
        result.append(i)
print(len(result))
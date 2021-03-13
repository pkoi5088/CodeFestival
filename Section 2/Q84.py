from itertools import combinations

l=list(input())
k=int(input())
f=list(map(''.join,combinations(l,k)))
tmp=-1

for i in f:
    if tmp<int(i):
        tmp=int(i)
print(tmp)
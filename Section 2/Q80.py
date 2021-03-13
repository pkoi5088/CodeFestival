from itertools import combinations

l=input().split(',')
n=int(input())
print(list(map(''.join,combinations(l,n))))
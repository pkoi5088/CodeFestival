def solve():
    result=0
    for num in range(1001):
        result+=str(num).count('1')
    return result

print(solve())

# def count(n):
# 	countN = str(list(range(n+1))).count('1')
# 	return countN

# print(count(1000))
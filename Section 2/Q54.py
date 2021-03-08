def solve():
    for i in range(len(nums)-1):
        if nums[i+1]-nums[i]!=1:
            return 'NO'
    return 'YES'

nums=list(map(int,input().split()))
nums.sort()
print(solve())
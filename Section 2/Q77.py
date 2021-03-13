s1=input()
s2=input()

dp=[[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

for idxS1 in range(len(s1)):
    for idxS2 in range(len(s2)):
        if s1[idxS1]==s2[idxS2]:
            dp[idxS1+1][idxS2+1] = dp[idxS1][idxS2]+1
        else:
            dp[idxS1+1][idxS2+1] = max(dp[idxS1+1][idxS2],dp[idxS1][idxS2+1])

print(dp[len(s1)][len(s2)])
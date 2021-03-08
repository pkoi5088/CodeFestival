sum=0
for i in range(1,21):
    s=list(str(i))
    for j in s:
        sum+=int(j)
print(sum)
prime=[]

#n보다 같거나 작은 소수를 prime에 추가
def getPrime(n):
    numbers=[True for i in range(n+1)]
    for i in range(2,n+1):
        if numbers[i]==True:
            prime.append(i)
            for j in range(2*i,n+1,i):
                numbers[j] = False

def goldbach(n):
    for i in range(1,len(prime)):
        for j in range(0,i):
            if n==prime[i]+prime[j]:
                print("{} == {} + {}".format(n,prime[i],prime[j]))

n=int(input())
getPrime(n)
goldbach(n)
def sieve(n):
    prime=[True for i in range(n+1)]
    for i in range(2,len(prime)):
        if prime[i]==True:
            for j in range(i*i,len(prime),i):
                prime[j]=False
    return prime
prime=sieve(int(input("enter the lower bound")))
for i in range (len(prime)):
    if (prime[i]):
        print(i)
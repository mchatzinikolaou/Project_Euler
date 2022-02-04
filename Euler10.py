def isPrime(primes, number):
    isprime = True
    for prime in primes:
        if(prime<=num//2):
            if number % prime == 0:
                isprime = False

    if isprime:
        primes.append(number)
        print(num)
    return primes


num=3
primes=[2]
print(sum(primes))

while(num<2e06):
    primes=isPrime(primes,num)
    num=num+2

print(sum(primes))


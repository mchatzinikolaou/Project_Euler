


def isPrime(primes, number):
    isprime = True
    for prime in primes:
        if number % prime == 0:
            isprime = False

    if isprime:
        primes.append(number)
    return primes

num=3
primes=[2]
nth=10001

while(len(primes)<nth):
    primes=isPrime(primes,num)
    num=num+2
print(primes[-1])


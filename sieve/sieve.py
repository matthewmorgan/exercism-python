def sieve(limit):
    return list(filter(isPrime, range(2,limit+1)))

def isPrime(n):
    return len(list(filter(lambda f: n % f == 0, range(2, n)))) == 0
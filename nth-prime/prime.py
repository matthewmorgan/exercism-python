from math import log


def nth_prime(n):
    if n < 1:
        raise ValueError('Prime is not possible')
    elif n == 1:
        return 2
    # see http://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
    approximate_limit = max(15, int(n * log(n) + n * log(log(n))))
    return sieve(approximate_limit)[n-1]
    
def sieve(limit):
    p = 2
    span = [False, False] + [True] * limit
    primes = []

    for ii in range(2, int(limit / 2) + 1):
        for jj in range(2 * p, limit + 1, p):
            span[jj] = False
        p += 1

    for index, flag in enumerate(span):
        if flag:
            primes.append(index)
    return primes

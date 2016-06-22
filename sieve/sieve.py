def sieve(limit):
    p = 2
    span = [False, False]
    primes = []
    for ii in range(2, limit + 1):
        span.append(True)

    for ii in range(2, int(limit / 2) + 1):
        for jj in range(2 * p, limit + 1, p):
            span[jj] = False
        p += 1

    for index, flag in enumerate(span):
        if flag:
            primes.append(index)
    return primes
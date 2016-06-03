def sum_of_multiples(limit, factors = [3, 5]):
    multiples = set([0])
    current = limit - 1
    while current > 0:
        for factor in factors:
            if factor != 0 and current % factor == 0:
                multiples.add(current)
        current = current - 1
    return sum(multiples)
def prime_factors(num):
    factors = []
    current_factor = 2
    while num > 1:
        if num % current_factor == 0:
            factors.append(current_factor)
            num /= current_factor
        else:
            current_factor += 1
    return factors

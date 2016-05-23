def largest_product(k, n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError()
    l = len(k) // n * n
    return max([product(k[i:i+n], n) for i in range(0, l, 1)])


def product(l, n):
    p = 1
    for x in l:
        p *= int(x)
    return p

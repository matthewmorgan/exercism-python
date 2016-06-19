from numpy import mat, array, dot


def is_triplet(maybe):
    a, b, c = sorted(maybe)
    return a ** 2 + b **2 == c **2


def triplets_in_range(mn, mx):
    too_many = [tuple(sorted(t.tolist())) for t in triplet_generator(mx)]
    return set(filter(lambda t: all(mn <= side <= mx for side in t), too_many)) 


def primitive_triplets(x):
    if not x % 4 == 0:
        raise ValueError()
    too_many = primitive_triplet_generator(x ** 2)
    results = set()
    for (a, b, c) in too_many:
        if a == x or b == x:
            results.add(tuple(sorted((a, b, c))))
    return results

# SO http://stackoverflow.com/a/8263898/3084820
def triplet_generator(limit):
    for p in primitive_triplet_generator(limit):
        i = p
        for _ in range(limit//p[2]):
            yield i
            i = i + p

             
def primitive_triplet_generator(mx=None):
    u = mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = mat(' 1  2  2;  2  1  2; 2 2 3')
    d = mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = array([u, a, d])
    m = array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if mx:
            m = m[m[:, 2] <= mx]
        yield from m
        m = dot(m, uad)


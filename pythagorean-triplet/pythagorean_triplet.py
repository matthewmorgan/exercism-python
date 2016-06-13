SQUARES = [x**2 for x in range(0, 500)]


def is_triplet(maybe):
    (a, b, c) = (sorted(maybe))
    return SQUARES[a] + SQUARES[b] == SQUARES[c]


def primitive_triplets(x):
    sq_x = SQUARES[x]
    triplets = []
    for sq_y in SQUARES[1:]:
        if sq_x + sq_y in SQUARES[1:]:
            triplets.append(tuple(sorted((x, SQUARES.index(sq_y), SQUARES.index(sq_x+sq_y)))))
    return triplets


def triplets_in_range(m, n):
    triplets = []
    for a in range(m, n):
        sq_a = SQUARES[a]
        for b in range(a, n):
            sq_b = SQUARES[b]
            if sq_a + sq_b in SQUARES[1:]:
                triplets.append(tuple(sorted(a, b, SQUARES.index(sq_a + sq_b))))
    return triplets

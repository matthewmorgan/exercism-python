INTS = { '0': 0, '1': 1, '2': 2 }
BASE = 3

def trinary(tri_value='0'):
    if set(tri_value).difference(set(INTS.keys())):
        tri_value = '0'
    return sum([INTS[b]* BASE ** p for p, b in enumerate(reversed(list(tri_value)))])

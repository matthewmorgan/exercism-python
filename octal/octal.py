INTS = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7 }
BASE = 8

def parse_octal(octal='0'):
    if set(octal).difference(set(INTS.keys())):
        raise ValueError('Not a valid octal')
    return sum([INTS[b]* BASE ** p for p, b in enumerate(reversed(list(octal)))])
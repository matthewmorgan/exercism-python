INTS = { '0': 0, '1': 1 }
BASE = 2

def parse_binary(binary='0'):
    if set(binary).difference(set(INTS.keys())):
        raise ValueError()
    return sum([INTS[b]* BASE ** p for p, b in enumerate(reversed(list(binary)))])

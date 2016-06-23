BASE = 16
INTS = dict(zip('0123456789abcdef', range(0, BASE)))

def hexa(hex_value='0'):
    if set(hex_value.lower()).difference(set(INTS.keys())):
        raise ValueError('Not a valid hexadecimal')
    return sum([INTS[b]* BASE ** p for p, b in enumerate(reversed(list(hex_value.lower())))])
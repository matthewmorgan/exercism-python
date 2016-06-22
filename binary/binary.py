from re import fullmatch


def parse_binary(binary='0'):
    if not fullmatch(r'[01]+', binary):
        raise ValueError()
    return sum([2 ** p if b == '1' else 0 for p, b in enumerate(reversed(list(binary)))])

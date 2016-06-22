from re import fullmatch


def parse_binary(binary='0'):
    if not fullmatch(r'[01]+', binary):
        raise ValueError()
    return sum([int(b) * 2 ** p for p, b in enumerate(reversed(list(binary)))])

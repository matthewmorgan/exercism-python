import re
from functools import reduce


def encode(input):
    return ''.join(reduce(compress, tokenize(input), []))


def decode(input):
    return reduce(expand, chunk(input), '')


def tokenize(input):
    return re.finditer(r'(.)\1*', input)


def chunk(input):
    return re.findall(r'(\d*)(\D)', input)


def compress(output, match):
    return output + [('{}{}'.format(len(match.group()), match.group()[0]))] if len(match.group()) > 1 \
        else output + [match.group()]


def expand(a, b):
    return a + b[1] if not b[0] \
        else a + (b[1] * int(b[0]))

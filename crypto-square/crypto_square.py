from math import sqrt, ceil


def encode(phrase):
    if not phrase:
        return ''
    cleaned = ''.join(filter(str.isalnum, phrase.lower()))
    cols = ceil(sqrt(len(cleaned)))
    return ' '.join([cleaned[c::cols] for c in range(cols)])

from math import sqrt, ceil
from re import sub


def encode(phrase):
    if not phrase:
        return ''
    phrase = sub(r'[^a-z0-9]+', '', phrase)
    cols = ceil(sqrt(len(phrase)))
    rows = ceil(len(phrase)/cols)
    return phrase, cols, rows

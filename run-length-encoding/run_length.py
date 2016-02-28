import re
from functools import reduce

def encode(input):

    length = len(input)
    if length == 0:
        return ''
    if length == 1:
        return input

    compressed = ''
    previous_letter = input[0]
    duplicate_count = 0
    current_index = 0
    
    while current_index <= length:
        if current_index == length:
            if duplicate_count > 1:
                compressed += str(duplicate_count)
            compressed += previous_letter
        else:
            current_letter = input[current_index]
            if current_letter != previous_letter:
                if duplicate_count > 1:
                    compressed += str(duplicate_count)
                compressed += previous_letter
                previous_letter = current_letter
                duplicate_count = 1
            else:
                duplicate_count += 1
        current_index += 1
    return compressed

def decode(input):
    expand = lambda a, b: a + b[1] if not b[0] else a + (b[1] * int(b[0]))
    return reduce(expand, re.findall(r'(\d*)(\D)', input), '')





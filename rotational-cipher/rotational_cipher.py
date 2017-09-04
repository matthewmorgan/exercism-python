ALPHA_LENGTH = 26
ALPHA_START = 97


def rotate(value, offset):
    return ''.join([map_letter(letter, offset) for letter in value])


def map_letter(letter, offset):
    if not letter.isalpha():
        return letter
    return encode(letter.lower(), offset).upper() if letter.isupper() else encode(letter, offset)


def encode(letter, offset):
    return chr((ord(letter) - ALPHA_START + offset) % ALPHA_LENGTH + ALPHA_START)
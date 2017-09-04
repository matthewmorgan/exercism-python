def rotate(value, offset):
    return ''.join([map(letter, offset) for letter in value])

def map(value, offset):
    if not value.isalpha():
        return value
    if value.lower() != value:
        value = value.lower()
        return chr((ord(value) - 97 + offset) % 26 + 97).upper()
    return chr((ord(value) - 97 + offset) % 26 + 97)
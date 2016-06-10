import string
import random

A_VALUE = ord('a')
DEFAULT_SHIFT_DISTANCE = 3
ALPHA_LOWER_BOUND = 97
ALPHA_UPPER_BOUND = 122
ALPHABET_LENGTH = 26

class Caesar:
    def encode(self, plain_text):
        return ''.join([shift(letter) for letter in plain_text])

    def decode(self, cipher_text):
        return ''.join([shift(letter, -DEFAULT_SHIFT_DISTANCE) for letter in cipher_text])


class Cipher:
    def __init__(self, key=''):
        if key and not (key.isalpha() and key.lower() == key):
            raise ValueError
        self.key = key or Cipher.generate_random_key()

    def encode(self, plain_text):
        self.cipher = self.distance()
        return ''.join([shift(letter, next(self.cipher)) for letter in plain_text])

    def decode(self, cipher_text):
        self.cipher = self.distance(sign=-1)
        return ''.join([shift(letter, next(self.cipher)) for letter in cipher_text])

    def distance(self, sign=1):
        while True:
            for mapping in self.key:
                yield sign * (ord(mapping) - A_VALUE)

    @staticmethod
    def generate_random_key():
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(100))


def shift(letter, distance=DEFAULT_SHIFT_DISTANCE):
    lower_letter = letter.lower()
    ascii_code = ord(lower_letter)
    if ALPHA_LOWER_BOUND <= ascii_code <= ALPHA_UPPER_BOUND:
        new_code = (ord(lower_letter) + distance)
        if new_code > ALPHA_UPPER_BOUND:
            return chr(new_code - ALPHABET_LENGTH)
        elif new_code < ALPHA_LOWER_BOUND:
            return chr(new_code + ALPHABET_LENGTH)
        return chr(new_code)
    else:
        return ''



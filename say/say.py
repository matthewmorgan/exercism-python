import math

ONES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
PLACENAMES = ['', 'thousand', 'million', 'billion']


def say(num):
    if not num:
        return 'zero'

    num = int(float(num))
    if num < 0 or num > 999999999999:
        raise AttributeError('Number must be between 0 and 999,999,999,999')

    english = parse_number(num)
    if english.startswith('and '):
        english = english[4:]
    return english


def split_by_powers(digits: str):
    m = math.pow(10, len(digits))
    powers = [0, 0, 0]
    while len(digits) > 0:
        digit = digits[0]
        digits = digits[1:len(digits)]
        m = int(m // 10)
        powers[len(digits)] = int(digit) * m
    return powers


def extract_triplets(num: str):
    triplets = []
    remainder_length = len(num) % 3
    if remainder_length:
        triplets.append(''.join(num[0:remainder_length]))
    num = num[remainder_length: len(num)]
    while num:
        triplets.append(''.join(num[0:3]))
        num = num[3: len(num)]
    return triplets


def parse_number(num: int):
    place_name_index = 0
    english = []
    for triplet in reversed(extract_triplets(str(num))):
        phrase = parse_triplet_to_words(triplet, prepend_and=place_name_index == 0)
        if phrase:
            phrase += ' ' + PLACENAMES[place_name_index]
            english.append(phrase.strip())
        place_name_index += 1
    return ' '.join(reversed(english))


def parse_triplet_to_words(num: str, prepend_and: bool):
    powers = split_by_powers(num)
    segments = ['', '', '']
    if powers[1] == 10:
        teen_index = 10 + powers[0]
        segments[0] = ONES[teen_index]
    else:
        segments[0] = ONES[powers[0]]
        if powers[1]:
            segments[1] = TENS[int(powers[1] / 10)]
    if segments[1] and segments[0]:
        hyphenated = '-'.join(reversed(segments[0:2]))
        segments = ['', hyphenated, '']
    if powers[2]:
        segments[2] = ONES[int(powers[2] / 100)] + ' hundred'
        prepend_and = True
    if prepend_and:
        if segments[1]:
            segments[1] = 'and ' + segments[1]
        elif segments[0]:
            segments[0] = 'and ' + segments[0]
    return ' '.join(list(reversed(list(filter(None, segments)))))
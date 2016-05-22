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

    english = parse(num)
    if english.startswith('and '):
        english = english[4:]
    return english


def split_by_powers(num):
    digits = str(num)
    m = math.pow(10, len(digits))
    converted = []
    while len(digits) > 0:
        digit = digits[0]
        digits = digits[1:len(digits)]
        m = int(m // 10)
        converted.append(int(digit) * m)
    return list(reversed(converted))


def extract_brackets(num):
    digits = str(num)
    brackets = []
    endpoint = len(digits) % 3
    if endpoint:
        brackets.append(''.join(digits[0:endpoint]))
    digits = digits[endpoint: len(digits)]
    while len(digits) > 0:
        brackets.append(''.join(digits[0:3]))
        digits = digits[3: len(digits)]
    return brackets


def parse(num):
    brackets = extract_brackets(num)
    place_name_index = 0
    english = []
    for digits in reversed(brackets):
        prepend_and = place_name_index == 0
        phrase = parse_thousand(digits, prepend_and) + ' '
        if len(phrase.strip()) > 0:
            phrase += PLACENAMES[place_name_index]
            english.append(phrase.strip())
        place_name_index += 1
    return ' '.join(reversed(english))


def parse_thousand(num, prepend_and=False):
    powers = split_by_powers(int(num))
    segments = ['', '', '']
    if len(powers) > 1 and powers[1] == 10:
        index = 10 + powers[0]
        segments[0] = ONES[index]
    else:
        segments[0] = ONES[powers[0]]
        if len(powers) > 1:
            segments[1] = TENS[int(powers[1] / 10)]
    if segments[1] and segments[0]:
        hyphenated = '-'.join(reversed(segments[0:2]))
        segments = ['', hyphenated, '']
    if len(powers) > 2 and powers[2]:
        segments[2] = ONES[int(powers[2] / 100)] + ' hundred'
        prepend_and = True
    if prepend_and:
        if segments[1]:
            segments[1] = 'and ' + segments[1]
        elif segments[0]:
            segments[0] = 'and ' + segments[0]
    return ' '.join(list(reversed(list(filter(None, segments)))))

from collections import OrderedDict
import math

UNDER_TWENTY = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
                'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = OrderedDict({20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}).__reversed__()
POWERS = OrderedDict({100: 'hundred', 1000: 'thousand', 1000000: 'million', 1000000000: 'billion'}).__reversed__()


def say(number):
    result = ''
    while number >= 100:
        (result, number) = deduct_100_plus(result, number)
    while number >= 20:
        (result, number) = deduct20Plus(result, number)
        if 10 > number > 0:
            result += '-'
    while number >=1:
        (result, number) = (result + UNDER_TWENTY[number], number)

    return result


def deduct_100_plus(result, number):
    for p in POWERS:
        if number >= p:
            this_part = math.floor(number/p)
            (result, number) = deduct20Plus(result, number)
            result += POWERS[p]
        return result, number


def deduct20Plus(result, number):
    for p in TENS:
        if number >= p:
            this_part = math.floor(number/p)
            (result, number) = deductplus(result, number)
            result += POWERS[p]
    return result, number



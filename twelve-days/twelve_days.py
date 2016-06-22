DAYS = ['first', 'second','third','fourth','fifth','sixth',
        'seventh','eighth','ninth','tenth','eleventh','twelfth']

GIFTS = [
        'a Partridge in a Pear Tree',
        'two Turtle Doves',
        'three French Hens',
        'four Calling Birds',
        'five Gold Rings',
        'six Geese-a-Laying',
        'seven Swans-a-Swimming',
        'eight Maids-a-Milking',
        'nine Ladies Dancing',
        'ten Lords-a-Leaping',
        'eleven Pipers Piping',
        'twelve Drummers Drumming'
        ]


def sing():
    return verses(1, len(DAYS))


def verse(num):
    song = _get_beginning(num) + ''.join([_nth_gift(n) for n in range(num, 1, -1)])
    song += '{}{}.\n'.format('and ' if num > 1 else '', GIFTS[0])
    return song


def verses(first, last):
    return ''.join([verse(n)+'\n' for n in range(first, last+1)])


def _get_beginning(n):
    return 'On the {} day of Christmas my true love gave to me, '.format(DAYS[n-1])


def _nth_gift(n):
    return '{}, '.format(GIFTS[n-1])
    
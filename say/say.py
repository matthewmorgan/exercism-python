def say(number):
    result =''
    while number >= 100:
        result += 'one hundred'
        number -= 100
        if number >= 20:
            result += ' and '
    while number >= 20:
        result += 'twenty'
        number -= 20
        if number > 0:
            result += '-'
    while number >= 14:
        result += 'fourteen'
        number -= 14
    while number >= 2:
        result += 'two'
        number -= 2
    while number >= 1:
        result += 'one'
        number -= 1

    return result

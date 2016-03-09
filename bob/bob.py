def hey(what):

    cleaned = what.strip()

    if (cleaned.isupper()):
        return 'Whoa, chill out!'

    if (cleaned.endswith('?')):
        return 'Sure.'

    if (cleaned == ''):
        return 'Fine. Be that way!'

    return 'Whatever.'

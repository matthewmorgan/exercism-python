import re

response_to = {'shout': 'Whoa, chill out!', 'question': 'Sure.',
               'silence': 'Fine. Be that way!', 'anything else': 'Whatever.'}
alpha = re.compile('[a-z]+', re.I)

def hey(what):

    cleaned = what.strip()

    if (re.search(alpha, cleaned) and cleaned.upper() == cleaned):
        return response_to['shout']

    last_index = len(cleaned) - 1
    if (len(cleaned) > 0 and cleaned[last_index] == '?'):
        return response_to['question']

    if (len(cleaned) == 0):
        return response_to['silence']

    return response_to['anything else']

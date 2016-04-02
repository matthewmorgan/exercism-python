import re

def abbreviate(phrase):
    firsts = re.findall(r'[A-Z]+[a-z]*|[a-z]+', phrase)
    return ''.join(map(lambda word: word[0], firsts)).upper()
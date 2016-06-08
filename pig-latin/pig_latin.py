import re


def translate(english):
    translated = []
    for word in english.split():
        beginning = re.match(r'^(?:[aeiou])|(?:xr)|(?:yt)|(ch|sch|squ|qu|thr|th|[bcdfghjklmnprstvwxyz])', word).groups()[0] or ''
        translated.append(word[len(beginning):]+beginning+'ay')
    return ' '.join(translated)
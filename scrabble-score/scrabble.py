letters = 'aeioulnrstdgbcmpfhvwykjxqz'
scores = '111111111122333344444588aa'
table = str.maketrans(letters, scores)


def score(word):
    if not word.isalpha():
        word = ''
    return sum([int(s, 16) for s in str.translate(word.lower(), table)])
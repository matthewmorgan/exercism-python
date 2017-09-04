def is_isogram(phrase):
    letters_only = list(filter(str.isalpha, phrase))
    unique__lowercase_letters = list(filter(str.isalpha, set(phrase.lower())))
    return len(unique__lowercase_letters) == len(letters_only)

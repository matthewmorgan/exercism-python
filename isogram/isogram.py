def is_isogram(phrase):
    lowercase_letters_only = list(filter(str.isalpha, phrase.lower()))
    return len(set(lowercase_letters_only)) == len(lowercase_letters_only)

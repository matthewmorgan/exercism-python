def is_isogram(phrase):
    lowercase_letters_only = [letter for letter in phrase.lower() if letter.isalpha()]
    return len(set(lowercase_letters_only)) == len(lowercase_letters_only)

alphabet_length = 26


def is_pangram(sentence:str) -> bool:
    return len(set(filter(str.isalnum, sentence))) >= alphabet_length
sort_word = lambda word: ''.join(sorted(word))

def detect_anagrams(word, candidates):
    global sorted_word, original_word
    original_word = word.lower
    sorted_word  = sort_word(word).lower
    return list(filter(is_anagram, candidates))

def is_anagram(candidate):
    return sorted_word == sort_word(candidate)  and not_same(candidate)

def not_same(candidate):
    return original_word != candidate


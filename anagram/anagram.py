def detect_anagrams(word, candidates):
    global sorted_word, original_word
    original_word = word.lower()
    sorted_word  = sort_word(word).lower()
    return list(filter(is_anagram, candidates))

def is_anagram(candidate):
    return sorted_word == sort_word(candidate) and not_original_word(candidate)

def not_original_word(candidate):
    return original_word != candidate.lower()

sort_word = lambda word: ''.join(sorted(word.lower()))
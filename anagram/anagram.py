def detect_anagrams(word, candidates):
    original = word.casefold()
    letters  = sorted(original)
    return [c for c in candidates if is_anagram(original, letters, c)]

def is_anagram(original, letters, candidate): 
    return letters == sorted(candidate.casefold()) and original != candidate.casefold()
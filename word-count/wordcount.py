import re

unicode_letters = re.compile('[^_\W]+', re.IGNORECASE | re.UNICODE)

def word_count(phrase):
  words = re.findall(unicode_letters, phrase.lower())
  counts = {}
  for word in words:
    counts[word] = counts.get(word, 0) + 1
  return counts
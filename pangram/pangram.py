import re

alphabet_length = 26
non_alphas = re.compile('[^a-z]+')

def is_pangram(sentence):
  lowercase = sentence.lower()
  cleaned = set(re.sub(non_alphas, '', lowercase))
  return len(cleaned) == alphabet_length
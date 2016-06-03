alphabet = list('abcdefghijklmnopqrstuvwxyz')
key = list(alphabet[::-1])
CHUNK_SIZE = 5

clean = lambda c: c.lower() if c.isalnum() else ''
encode_char = lambda c: key[alphabet.index(c)] if c.isalpha() else c
decode_char = lambda c: alphabet[key.index(c)] if c.isalpha() else '' if c == ' ' else c
chunk = lambda text: [text[i:i+CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]

def encode(phrase):
    clean_phrase = ''.join(map(clean, phrase))
    chunks = chunk(''.join(map(encode_char, clean_phrase)))
    return ' '.join(chunks)

def decode(phrase):
    return ''.join(map(decode_char, list(phrase)))
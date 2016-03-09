from functools import reduce

foldl = lambda total, pair: total if pair[0] == pair[1] else total + 1

def distance(strand1, strand2):
  return reduce(foldl, zip(strand1, strand2), 0)


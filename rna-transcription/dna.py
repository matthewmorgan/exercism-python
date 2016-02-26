D = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
f = lambda a: D[a]

def to_rna(dna):
  rna_map = map(f, dna)
  return ''.join(rna_map)
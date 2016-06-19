class Matrix:
    def __init__(self, input):
        self.parse(input)
    
    def parse(self, input):
        self.rows = [[int(el) for el in row.split(' ')] for row in input.splitlines()]
        self.columns= [list(tup) for tup in zip(*self.rows)]

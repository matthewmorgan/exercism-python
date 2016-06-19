class Matrix:
    def __init__(self, data):
        self.rows = [[int(el) for el in row.split(' ')] for row in data.splitlines()]
        self.columns= [list(tup) for tup in zip(*self.rows)]
        

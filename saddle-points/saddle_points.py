def saddle_points(matrix):    
    if not matrix:
        return set()
    column_count = len(matrix[0])
    if not all([len(row) == column_count for row in matrix]):
        raise ValueError()
    
    row_maxes = set()
    col_mins = set()
    
    for row_num, row in enumerate(matrix):
        [row_maxes.add((row_num, col_num)) for col_num, el in enumerate(row) if el == max(row)]
        
    for col_num, col in enumerate(zip(*matrix)):
        [col_mins.add((row_num, col_num)) for row_num, el in enumerate(col) if el == min(col)]

    return col_mins.intersection(row_maxes)
    
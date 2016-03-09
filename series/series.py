def slices(input_string, size):
    
    if size < 1 or size > len(input_string):
        raise ValueError
    
    first_index = 0
    last_index = size
    int_source = [int(x) for x in list(input_string)]
    result = []
    
    while last_index <= len(int_source):
        result.append(int_source[first_index:last_index])
        last_index += 1
        first_index += 1
        
    return result
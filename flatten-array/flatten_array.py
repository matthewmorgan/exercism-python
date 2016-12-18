def flatten(arr):
    result = []
    for el in arr or []:
        result.append(el) if type(el) in [int, str] else result.extend(flatten(el))
    return result

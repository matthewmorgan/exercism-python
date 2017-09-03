def flatten(arr):
    if arr is None:
        return []
    result = []
    for el in arr:
        result.append(el) if type(el) in [int, str] else result.extend(flatten(el))
    return result

def flatten(arr):
    result = []
    for el in arr or []:
        result.append(el) if isinstance(el, int) or isinstance(el, str) else result.extend(flatten(el))
    return result

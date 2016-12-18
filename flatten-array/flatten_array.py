def flatten(arr):
    arr = arr or []
    result = []
    for el in arr:
        result.append(el) if isinstance(el, int) or isinstance(el, str) else result.extend(flatten(el))
    return result

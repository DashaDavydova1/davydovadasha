def filter_list(items):
    result = []
    for x in items:
        if isinstance(x, int):
            result.append(x)
    return result
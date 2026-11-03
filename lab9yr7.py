def only_one(*args):
    return sum (x is True for x in args) == 1
def unique_in_order(iterable):
    return [i[0] for i in __import__('itertools').groupby(iterable)]

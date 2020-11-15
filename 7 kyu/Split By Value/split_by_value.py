def split_by_value(k, elements):
    l = [i for i in elements if i < k]
    [elements.remove(i) for i in l]
    return l+elements

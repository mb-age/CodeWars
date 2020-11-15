def move_zeros(array):
    l = [i for i in array if isinstance(i,str) or '0' != str(i) != '0.0']
    return l + [0] * (len(array)-len(l))

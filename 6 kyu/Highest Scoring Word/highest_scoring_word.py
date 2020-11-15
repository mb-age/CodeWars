def high(x):
    y = [sum(ord(j)-96 for j in i) for i in x.split()]
    return x.split()[y.index(max(y))]

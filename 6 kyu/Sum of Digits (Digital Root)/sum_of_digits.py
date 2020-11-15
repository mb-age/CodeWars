def digital_root(n):
    return digital_root(sum(map(int,str(n)))) if n > 9 else n

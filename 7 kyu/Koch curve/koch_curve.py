def koch_curve(n):
    l = []
    for i in range(1, n + 1):
        l = l + [60] + l + [-120] + l + [60] + l
    return l

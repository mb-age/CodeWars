def sum_pairs(ints, s):
    if s%2:
        ints = list(set(ints))
    lst = []
    for i in range(len(ints)):
        for j in range(i+1, len(ints)):
            if ints[i] + ints[j] == s:
                lst.append([ints[i], ints[j]])
                ints = ints[:j]
                break
    return lst[-1] if lst else None

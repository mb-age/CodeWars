def find_it(seq):
    return sorted(list({i:seq.count(i)%2 for i in set(seq)}.items()), key=lambda x:x[1])[-1][0]

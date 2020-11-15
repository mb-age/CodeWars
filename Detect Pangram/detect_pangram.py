def is_pangram(s):
    l = []
    for i in set(s.lower()):
        if i.isalpha(): l.append(i)
    return len(l) == 26

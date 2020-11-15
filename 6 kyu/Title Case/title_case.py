def title_case(name, words=''):
    n = name.lower().split()
    l = [n[1:].index(i)+1 for i in words.lower().split() if i in n[1:]]
    n = [i.title() for i in n]
    for i in l:
        n[i] = n[i].lower()
    return ' '.join(n)

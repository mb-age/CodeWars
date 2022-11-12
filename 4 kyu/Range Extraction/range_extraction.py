def solution(args):
    s, l = [], []
    while len(args)-1:
        if args[0] == args[1] - 1:
            l.append(args[0])
            args.remove(args[0])
        else:
            if l:
                s.append(l)
                l = []
            s.append(args[0])
            args.remove(args[0])
    if l: s.append(l)
    s.append(args[-1])
    for i,j in enumerate(s):
        if type(j) == list and len(j) > 1:
            s[i] = f'{j[0]}-{j[-1]+1}'
            s.pop(i+1)
        elif type(j) == list:
            s[i] = j[0]
    s = ','.join(map(str,s))
    return s
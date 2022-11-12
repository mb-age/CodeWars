def snail(s):
    l = []
    while 1:
        l += [i for i in s[0]]
        s = s[1:]
        if not s: break
        l += [i[-1] for i in s]
        s = [i[:-1] for i in s]
        l += [i for i in s[-1][::-1]]
        s = s[:-1]
        if not s: break
        l += [i[0] for i in s[::-1]]
        s = [i[1:] for i in s]
    return l
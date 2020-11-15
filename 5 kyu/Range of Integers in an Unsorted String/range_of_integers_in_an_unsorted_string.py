def mystery_range(s,n):
    a = 0
    while True:
        l = ''.join(str(i) for i in range(a,n+a))
        if sorted(l) == sorted(s):
            if str(a)[::-1] == str(n+a) and \
            str(n+a) in [s[i]+s[i+1] for i in range(0,len(s)-1,2)]:
                return [a+1, n+a]
            return [a, n+a-1]
        else:
            a += 1

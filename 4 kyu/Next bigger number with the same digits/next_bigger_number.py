def next_bigger(n):
    n, m = str(n)[::-1], ''
    for i,j in enumerate(n[:-1],2):
        if j > n[i-1]:
            n,m = n[i:][::-1], n[:i][::-1]
            break
    if not m: return -1
    for i in m[1:]:
        if i > m[0]:
            n1, m1 = n+i, ''.join(sorted(m.replace(i,'',1)))
    return int(n1+m1)
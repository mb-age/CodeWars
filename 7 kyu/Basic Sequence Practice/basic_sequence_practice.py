def sum_of_n(n):
    l=[]
    s=0
    if n >= 0:
        for i in range(1,n+2):
            l.append(s)
            s += i
        return l
    else:
        for i in range(-1, n-2, -1):
            l.append(s)
            s += i
        return l

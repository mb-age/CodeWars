def decompose(n):
    l = []
    if n == '0': return l
    if '/' in n:
        num, den = map(int, n.split('/'))
    elif '.' in n:
        num, den = int(n.split('.')[1]), 10 ** len(n.split('.')[1])
        num += den * int(n.split('.')[0])
    if num >= den:
        l.append(str(num // den))
        num = num % den
    while num > 0:
        i = -(den//-num)
        l.append(f'1/{i}')
        num,den = (i*num-den), den*i
    return l
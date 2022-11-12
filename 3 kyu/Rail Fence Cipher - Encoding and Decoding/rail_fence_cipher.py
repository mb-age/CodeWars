from itertools import cycle, chain


def encode_rail_fence_cipher(string, n):
    iterator = cycle([*range(n - 1), *reversed(range(1, n))])

    l = [[] for _ in range(n)]
    for i, j in zip(string, iterator):
        l[j].append(i)
    l = ''.join([*chain(*l)])
    return l


def decode_rail_fence_cipher(string, n):
    iterator = cycle([*range(n - 1), *reversed(range(1, n))])

    l = [0 for _ in range(n)]
    for _, j in zip(range(len(string)), iterator): l[j] += 1

    k = []
    for i in l:
        k.append(string[:i])
        string = string[i:]

    l = [k[0], *[i[::2] for i in k[1:-1]], k[-1], *[i[1::2] for i in k[1:-1][::-1]]]

    k = ''
    for i in range(len(l[0])):
        for j in l:
            try:
                k += j[i]
            except:
                break

    return k
def swap(s, num):
    s = list(s)
    num = list(binar(num))
    iterator = -1
    for i in range(len(s)):
        if s[i].isalpha():
            iterator += 1
            if num[iterator] == '1': s[i] = s[i].swapcase()
        if iterator == len(num) - 1: iterator = -1
    return ''.join(s)


def binar(num):
    if num == 0: return '0'
    if num == 1: return '1'
    return str(binar(num // 2)) + str(num % 2)

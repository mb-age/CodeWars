def presses(phrase):
    l = 'ABCDEFGHIJKLMNOPQRTUVWXY10ZS23456879 '
    press = []
    for i in phrase.upper():
        if i in l[:26]:
            press.append(l.index(i)%3+1)
        elif i in l[26:34]:
            press.append(4)
        elif i in l[34:36]:
            press.append(5)
        else:
            press.append(1)
    return sum(press)

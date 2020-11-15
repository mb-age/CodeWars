def add(num1, num2):
    num1, num2 = str(num1)[::-1], str(num2)[::-1]
    return int(''.join([num1[len(num2):][::-1] if len(num1) > len(num2) else num2[len(num1):][::-1]] + [str(sum((int(i), int(j)))) for i, j in list(zip(list(num1), list(num2)))][::-1]))

def number(lines):
    num = 1
    for i in range(len(lines)):
        lines[i] = str(num)+": "+lines[i]
        num += 1
    return lines

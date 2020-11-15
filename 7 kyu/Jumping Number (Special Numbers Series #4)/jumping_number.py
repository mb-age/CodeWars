def jumping_number(number):
    n = str(number)
    return f"{['Not!!','Jumping!!'][all([int(n[i]) == int(n[i+1]) + 1 or int(n[i]) == int(n[i+1]) - 1 for i in range(len(n) - 1)])]}"

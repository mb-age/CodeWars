def solution(number):
    return sum(i for i in range(number) if not i%3 or not i%5)

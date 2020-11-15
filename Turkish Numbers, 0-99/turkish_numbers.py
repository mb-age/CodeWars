def get_turkish_number(num):
    units = ['sıfır', 'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz']
    tens = ['on', 'yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan']
    if num < 10:
        return units[num % 10]
    if num % 10 == 0:
        return tens[num // 10 - 1]
    return f'{tens[num // 10 - 1]} {units[num % 10]}'

from eureka import sum_dig_pow

def test_sum_dig_pow1():
    assert sum_dig_pow(1,10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_sum_dig_pow2():
    assert sum_dig_pow(1,100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

def test_sum_dig_pow3():
    assert sum_dig_pow(10,89) == [89]

def test_sum_dig_pow4():
    assert sum_dig_pow(10,100) == [89]

def test_sum_dig_pow5():
    assert sum_dig_pow(90,100) == []

def test_sum_dig_pow6():
    assert sum_dig_pow(89,135) == [89, 135]

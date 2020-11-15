from bit_counting import count_bits

def test_count_bits1():
    assert count_bits(0) == 0

def test_count_bits2():
    assert count_bits(4) == 1

def test_count_bits3():
    assert count_bits(7) == 3

def test_count_bits4():
    assert count_bits(9) == 2

def test_count_bits5():
    assert count_bits(10) == 2

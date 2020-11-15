from roman_numerals_encoder import solution

def test_solution1():
    assert solution(1) == 'I'

def test_solution2():
    assert solution(4) == 'IV'

def test_solution3():
    assert solution(6) == 'VI'

def test_solution4():
    assert solution(14) == 'XIV'

def test_solution5():
    assert solution(21) == 'XXI'

def test_solution6():
    assert solution(89) == 'LXXXIX'

def test_solution7():
    assert solution(91) == 'XCI'

def test_solution8():
    assert solution(984) == 'CMLXXXIV'

def test_solution9():
    assert solution(1000) == 'M'

def test_solution10():
    assert solution(1889) == 'MDCCCLXXXIX'

def test_solution11():
    assert solution(1989) == 'MCMLXXXIX'

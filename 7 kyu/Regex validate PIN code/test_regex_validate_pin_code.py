from regex_validate_pin_code import validate_pin

def test_validate_pin_wrong1():
    assert validate_pin('1') == False

def test_validate_pin_wrong2():
    assert validate_pin('12') == False

def test_validate_pin_wrong3():
    assert validate_pin('123') == False

def test_validate_pin_wrong4():
    assert validate_pin('12345') == False

def test_validate_pin_wrong5():
    assert validate_pin('1234567') == False

def test_validate_pin_wrong6():
    assert validate_pin('-1234') == False

def test_validate_pin_wrong7():
    assert validate_pin('1.234') == False

def test_validate_pin_wrong8():
    assert validate_pin('00000000') == False

def test_validate_pin_chars1():
    assert validate_pin('a234') == False

def test_validate_pin_chars2():
    assert validate_pin('.234') == False

def test_validate_pin_chars3():
    assert validate_pin('-123') == False

def test_validate_pin_chars4():
    assert validate_pin('-1.234') == False

def test_validate_pin_valid1():
    assert validate_pin('1234') == True

def test_validate_pin_valid2():
    assert validate_pin('0000') == True

def test_validate_pin_valid3():
    assert validate_pin('1111') == True

def test_validate_pin_valid4():
    assert validate_pin('123456') == True

def test_validate_pin_valid5():
    assert validate_pin('098765') == True

def test_validate_pin_valid6():
    assert validate_pin('000000') == True

def test_validate_pin_valid7():
    assert validate_pin('090909') == True

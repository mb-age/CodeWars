from jumping_number import jumping_number


def test_jumping_number_single_digit_number():
    assert jumping_number(1) == "Jumping!!"
    assert jumping_number(7) == "Jumping!!"
    assert jumping_number(9) == "Jumping!!"

def test_jumping_number_two_digit_number():
    assert jumping_number(23) == "Jumping!!"
    assert jumping_number(32) == "Jumping!!"
    assert jumping_number(98) == "Jumping!!"
    assert jumping_number(79) == "Not!!"

def test_jumping_number_larger_numbers():
    assert jumping_number(8987) == "Jumping!!"
    assert jumping_number(4343456) == "Jumping!!"
    assert jumping_number(98789876) == "Jumping!!"



from sum_of_digits import digital_root

def test_digital_root1():
    assert digital_root(16) == 7

def test_digital_root2():
    assert digital_root(942) == 6

def test_digital_root3():
    assert digital_root(132189) == 6

def test_digital_root4():
    assert digital_root(493193) == 2


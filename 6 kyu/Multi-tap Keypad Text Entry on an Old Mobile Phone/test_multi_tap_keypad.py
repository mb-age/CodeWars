from multi_tap_keypad import presses


def test_presses():
    assert presses("LOL") == 9

def test_presses2():
    assert presses("HOW R U") == 13


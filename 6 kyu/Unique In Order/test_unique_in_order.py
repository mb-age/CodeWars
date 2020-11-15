from unique_in_order import unique_in_order

def test_unique_in_order():
    assert unique_in_order('AAAABBBCCDAABBB') == ['A','B','C','D','A','B']



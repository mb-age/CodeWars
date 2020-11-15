from highest_scoring_word import high


def test_high1():
    assert high('man i need a taxi up to ubud') == 'taxi'

def test_high2():
    assert high('what time are we climbing up the volcano') == 'volcano'

def test_high3():
    assert high('take me to semynak') == 'semynak'


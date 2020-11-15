from title_case import title_case


def test_title_case_empty():
    assert title_case('') == ''

def test_title_case_lower_minor_words():
    assert title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings'

def test_title_case_title_minor_words():
    assert title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows'

def test_title_case_no_minor_words():
    assert title_case('the quick brown fox') == 'The Quick Brown Fox'

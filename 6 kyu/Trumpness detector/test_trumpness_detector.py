from trumpness_detector import trump_detector

def test_trump_detector_1():
    trump_speech = 'I will build a huge wall'
    result = 0
    assert trump_detector(trump_speech) == result

def test_trump_detector_2():
    trump_speech = 'HUUUUUGEEEE WAAAAAALL'
    result = 4
    assert trump_detector(trump_speech) == result

def test_trump_detector_3():
    trump_speech = 'MEXICAAAAAAAANS GOOOO HOOOMEEEE'
    result = 2.5
    assert trump_detector(trump_speech) == result

def test_trump_detector_4():
    trump_speech = 'America NUUUUUKEEEE Oooobaaaamaaaaa'
    result = 1.89
    assert trump_detector(trump_speech) == result

def test_trump_detector_5():
    trump_speech = 'listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT'
    result = 1.56
    assert trump_detector(trump_speech) == result


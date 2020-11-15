from moving_zeros_to_the_end import move_zeros


def test_move_zeros():
    assert move_zeros([1,2,0,1,0,1,0,3,0,1]) == [1,2,1,1,3,1,0,0,0,0]

def test_move_zeros_float():
    assert move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]) == [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]

def test_move_zeros_with_letters():
    assert move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]) == ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]

def test_move_zeros_with_none():
    assert move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]) == ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]

def test_move_zeros2():
    assert move_zeros([0,1,None,2,False,1,0]) == [1,None,2,False,1,0,0]

def test_move_zeros_only_letters():
    assert move_zeros(["a","b"]) == ["a","b"]

def test_move_zeros_one_letter():
    assert move_zeros(["a"]) == ["a"]

def test_move_zeros_only_zeroes():
    assert move_zeros([0,0]) == [0,0]

def test_move_zeros_one_zero():
    assert move_zeros([0]) == [0]

def test_move_zeros_one_bool():
    assert move_zeros([False]) == [False]

def test_move_zeros_empty_list():
    assert move_zeros([]) == []


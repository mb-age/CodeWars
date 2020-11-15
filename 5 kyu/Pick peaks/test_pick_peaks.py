from pick_peaks import pick_peaks

def test_pick_peaks():
    assert pick_peaks([1,2,3,6,4,1,2,3,2,1]) == {"pos":[3,7], "peaks":[6,3]}

def test_pick_peaks_with_edges():
    assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]) == {"pos":[3,7], "peaks":[6,3]}

def test_pick_peaks_two_peaks_and_plateu():
    assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]) == {"pos":[3,7,10], "peaks":[6,3,2]}

def test_pick_peaks_one_pick_and_plateu():
    assert pick_peaks([2,1,3,1,2,2,2,2,1]) == {"pos":[2,4], "peaks":[3,2]}

def test_pick_peaks_one_pick_and_plateu_till_the_edge():
    assert pick_peaks([2,1,3,1,2,2,2,2]) == {"pos":[2], "peaks":[3]}

def test_pick_peaks_one_pick_and_pick_till_the_edge():
    assert pick_peaks([2,1,3,2,2,2,2,5,6]) == {"pos":[2], "peaks":[3]}

def test_pick_peaks_one_pick():
    assert pick_peaks([2,1,3,2,2,2,2,1]) == {"pos":[2], "peaks":[3]}

def test_pick_peaks_four_picks():
    assert pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]) == {"pos":[2,7,14,20], "peaks":[5,6,5,5]}

def test_pick_peaks_empty_arrow():
    assert pick_peaks([]) == {"pos":[],"peaks":[]}

def test_pick_peaks_just_plateu():
    assert pick_peaks([1,1,1,1]),{"pos":[],"peaks":[]}



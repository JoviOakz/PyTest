from App import sum, sub, div, mul

def test_sum():
    assert sum(1, 2) == 3
    assert sum(1, 1) != 3
    assert sum(8, -2) == 6

def test_sub():
    assert sub(4, 2) == 2
    assert sub(1, 2) == -1
    assert sub(7, -2) == 9

def test_div():
    assert div(1, 2) == 0.5
    assert div(3, 2) == 1.5
    assert div(8, 2) == 4
    
def test_mul():
    assert mul(1, 2) == 2
    assert mul(3, 2) == 6
    assert mul(4, 2) == 8
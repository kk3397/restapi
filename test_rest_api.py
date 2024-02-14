import equations


def test_tri_area():
    assert equations.trian_area(5, 10) == 25
    assert equations.trian_area(10, 50) == 250


def test_tri_perm():
    assert equations.perm_tri(5, 10, 20) == 35
    assert equations.perm_tri(10, 50, 1000) == 1060


def test_rec_area():
    assert equations.rect_area(25, 25) == 625
    assert equations.rect_area(0, 90) == 0


def test_rec_perm():
    assert equations.perm_rec(15, 0, ) == 30
    assert equations.perm_rec(10, 50) == 120

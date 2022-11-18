from distance import distance


def test_distance_the_same():
    assert distance(10, (2, 3), (2, 3)) == 0


def test_distance_NE_NE_1():
    assert distance(10, (2, 3), (5, 1)) == 5


def test_distance_NE_NE_2():
    assert distance(20, (7, 3), (4, 5)) == 5


def test_distance_NW_NW_1():
    assert distance(15, (-5, 4), (-2, 5)) == 4


def test_distance_NW_NW_2():
    assert distance(10, (-5, 4), (-2, 5)) == 4


def test_distance_SE_SE_1():
    assert distance(12, (-3, 4), (-5, 1)) == 5


def test_distance_SE_SE_2():
    assert distance(12, (-4, 1), (-3, 3)) == 3


def test_distance_SW_SW_1():
    assert distance(14, (-8, -4), (-2, -6)) == 8


def test_distance_SW_SW_2():
    assert distance(14, (-2, -6), (-5, -2)) == 7


def test_distance_NE_SE():
    assert distance(10, (2, 4), (5, -2)) == 9


def test_distance_NE_SE_around():
    assert distance(10, (2, 6), (5, -8)) == 10


def test_distance_NW_SW():
    assert distance(14, (-2, 6), (-5, 2)) == 7


def test_distance_NW_SW_around():
    assert distance(14, (-2, 8), (-5, -9)) == 15


def test_distance_NW_NE():
    assert distance(14, (-2, 6), (5, 2)) == 11


def test_distance_NW_NE_around():
    assert distance(14, (-2, 6), (13, 2)) == 18


def test_distance_SW_SE():
    assert distance(14, (-2, -6), (5, -2)) == 11


def test_distance_SW_SE_around():
    assert distance(14, (-13, -6), (5, -2)) == 15

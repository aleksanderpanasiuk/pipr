from distance import flat_distance


def test_flat_distance_typical():
    assert flat_distance(-2, 2, 10) == 4


def test_flat_distance_around():
    assert flat_distance(-9, 9, 10) == 3


def test_flat_distance_zeroes():
    assert flat_distance(0, 0, 0) == 0


def test_flat_distance_small_board():
    assert flat_distance(-1, 1, 1) == 1

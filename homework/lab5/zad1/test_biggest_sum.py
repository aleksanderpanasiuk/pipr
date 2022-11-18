from biggest_sum import biggest_sum


def test_biggest_sum_typical():
    list = [1, 2, 3, 4, 5, 9, 7, 8, 1]
    assert biggest_sum(3, list) == 24


def test_biggest_sum_first():
    list = [10, 21, 3, 4, 5, 6, 7, 8, 9]
    assert biggest_sum(4, list) == 38


def test_biggest_sum_last():
    list = [1, 2, 3, 4, 5, 6, 9, 9, 9]
    assert biggest_sum(3, list) == 27


def test_biggest_sum_all_elements_same():
    list = [1, 1, 1, 1, 1, 1]
    assert biggest_sum(4, list) == 4


def test_biggest_sum_empty_list():
    list = []
    assert biggest_sum(2, list) == 0


def test_biggest_sum_zero_n():
    list = [1, 2, 3, 3, 2, 1]
    assert biggest_sum(0, list) == 0


def test_biggest_sum_n_bigger_than_list_len():
    list = [2, 1, 3, 7, 6, 9]
    assert biggest_sum(20, list) == 28


def test_biggest_sum_n_zero_empyty_list():
    list = []
    assert biggest_sum(0, list) == 0

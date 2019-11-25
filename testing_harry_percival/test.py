from bowling import score


def test_all_zeros():
    assert score('00 00 00 00 00 00 00 00 00 00') == 0


def test_one_point():
    assert score('01 00 00 00 00 00 00 00 00 00') == 1


def test_more_than_one_point():
    assert score('04 00 00 00 00 00 00 00 00 00') == 4
    assert score('40 00 00 00 00 00 00 00 00 00') == 4

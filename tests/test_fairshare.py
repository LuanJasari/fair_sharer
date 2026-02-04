from fairsharer import fair_sharer


def test_fair_sharer_one_iteration():
    values = [0, 1000, 800, 0]
    result = fair_sharer(values, 1)
    assert result == [100, 800, 900, 0]


def test_fair_sharer_two_iterations():
    values = [0, 1000, 800, 0]
    result = fair_sharer(values, 2)
    assert result == [100, 890, 720, 90]


def test_fair_sharer_does_not_modify_original():
    values = [0, 1000, 800, 0]
    fair_sharer(values, 1)
    assert values == [0, 1000, 800, 0]

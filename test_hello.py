from hello import add, subtract, divide


def test_add():
    assert 2 == add(1, 1)


def test_subtract():
    assert 3 == subtract(7, 4)


def test_divide():
    assert 2 == divide(8, 4)

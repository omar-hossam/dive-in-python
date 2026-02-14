from myapp.core.calculator import add, multiply


def test_add():
    num1: int = 2
    num2: int = 3

    assert add(num1, num2) == 5


def test_add_2():
    assert add(12, 24) == 34


def test_mutliply():
    assert multiply(2, 3) == 6

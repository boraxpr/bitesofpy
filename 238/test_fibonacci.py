import pytest
from fibonacci import fib


def test_nlt0():
    with pytest.raises(ValueError):
        fib(-1)


def test_0():
    assert fib(0) == 0


def test_1():
    assert fib(1) == 1


def test_2():
    assert fib(2) == 1


def test_3():
    assert fib(3) == 2
# write one or more pytest functions below, they need to start with test_
import math
import pytest


@pytest.mark.ybr
def test_addition(input_val) -> None:
    y = 20
    assert input_val + y == 50


def test_sqrt() -> None:
    x = 25
    assert math.sqrt(x) == 5


@pytest.mark.parametrize("num, result", [(1, 11), (2, 22), (3, 33)])
def test_mutiplication(num, result):
    assert 11 * num == result


@pytest.mark.skip
def test_skip():
    i = 55
    assert i == 3


@pytest.mark.xfail
def test_xfail():
    f = 55
    assert f == 8

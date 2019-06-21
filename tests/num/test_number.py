
import numpy as np
from spx.num import *

def test_is_integer():
    assert is_integer(10)
    assert is_integer(10.0)
    assert not is_integer('a')
    assert not is_integer(10.5)
    assert is_integer(True)
    assert is_integer(False)

def test_is_not_integer():
    assert is_not_integer('a')
    assert not is_not_integer(False)
    assert not is_not_integer(True)
    assert not is_not_integer(10)
    assert not is_not_integer(10.0)
    assert is_not_integer(10.5)

def test_sum_n():
    assert sum_n(10) == 55


def test_sum_square_n():
    s = 1
    s += 2**2
    assert sum_square_n(2) == s
    s += 3**2
    assert sum_square_n(3) == s
    s += 4**2
    assert sum_square_n(4) == s


def test_ints_in_interval():
    # helper functions
    assert order_interval(2, 3.2) == (2, 3.2)
    assert order_interval(-2, -3.3) == (-3.3, -2)

    # closed interval
    assert ints_in_interval_cc(2, 3) == 2
    assert ints_in_interval_cc(3, 2) == 2
    assert ints_in_interval_cc(1.1, 2) == 1
    assert ints_in_interval_cc(1.1, 2.2) == 1
    assert ints_in_interval_cc(1, 2.2) == 2

    assert ints_in_closed_interval(2, 3) == 2
    assert ints_in_closed_interval(1.1, 2) == 1
    assert ints_in_closed_interval(1.1, 2.2) == 1
    assert ints_in_closed_interval(1, 2.2) == 2


    # closed open
    assert ints_in_interval_co(2, 3) == 1
    assert ints_in_interval_co(1.9, 3) == 1
    assert ints_in_interval_co(2, 3.1) == 2
    assert ints_in_interval_co(1.9, 3.1) == 2

    # open closed
    assert ints_in_interval_oc(2, 3) == 1
    assert ints_in_interval_oc(1.9, 3) == 2
    assert ints_in_interval_oc(2, 3.1) == 1
    assert ints_in_interval_oc(1.9, 3.1) == 2

    # open
    assert ints_in_interval_oo(2, 3) == 0
    assert ints_in_interval_oo(1.9, 3) == 1
    assert ints_in_interval_oc(2, 3.1) == 1
    assert ints_in_interval_oo(1.9, 3.1) == 2

    assert ints_in_open_interval(2, 3) == 0
    assert ints_in_open_interval(1.9, 3) == 1
    assert ints_in_open_interval(2, 3.1) == 1
    assert ints_in_open_interval(1.9, 3.1) == 2


def test_spectrum():
    x = 1.5
    s = spectrum_n(x, 4)
    s_true = np.array([1, 3, 4, 6])
    assert np.equal(s, s_true).all()

    x = 2 + math.sqrt(2)

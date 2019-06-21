import math
import numbers
import numpy as np

def is_int_type(x):
    """
    Returns if variable is of type integer
    """
    return isinstance(x, numbers.Integral)


def is_integer(x):
    """
    Returns if variable holds an integral value
    """
    if not isinstance(x, numbers.Number):
        return False
    if isinstance(x, numbers.Integral):
        return True
    if isinstance(x, numbers.Real):
        return x == math.floor(x)
    return False

def is_not_integer(x):
    if not isinstance(x, numbers.Number):
        return True
    return bool (math.ceil(x) - math.floor(x))

def sum_n(n):
    """
    Returns sum of first n natural numbers [starting from 1]
    """
    return n * (n + 1) / 2

def sum_square_n(n):
    """
    Returns sum of squares of first n natural numbers
    """
    return n * (n + 1) * (2 * n + 1) / 6



def ints_in_interval_cc(a, b):
    """
    Returns the number of integers in the closed interval [a, b]
    """
    # ensure that a and b are in proper order
    (a, b) = order_interval(a, b)
    return math.floor(b) - math.ceil(a) + 1

def ints_in_interval_co(a, b):
    """
    Returns the number of integers in the interval [a, b)
    """
    # ensure that a and b are in proper order
    (a, b) = order_interval(a, b)
    return math.ceil(b) - math.ceil(a)

def ints_in_interval_oc(a, b):
    """
    Returns the number of integers in the interval (a, b]
    """
    # ensure that a and b are in proper order
    (a, b) = order_interval(a, b)
    return math.floor(b) - math.floor(a)

def ints_in_interval_oo(a, b):
    """
    Returns the number of integers in the open interval (a, b)
    """
    # ensure that a and b are in proper order
    (a, b) = order_interval(a, b)
    return math.ceil(b) - math.floor(a) - 1


ints_in_closed_interval = ints_in_interval_cc
ints_in_open_interval = ints_in_interval_oo


def order_interval(a, b):
    """
    Order an interval a-b by ensuring that a <= b
    """
    if a > b:
        return (b, a)
    return (a, b)


def spectrum(x):
    """
    Returns the spectrum of a number
    """
    n = 0
    while True:
        n += 1
        yield math.floor(n*x)

def spectrum_n(x, n):
    """
    Returns the first n integers in the spectrum of a number
    """
    result = np.empty(n, dtype='int32')
    g  = spectrum(x)
    for i in range(n):
        result[i] = next(g)
    return result
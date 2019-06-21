"""
Some tests for basic numpy functionality

These are also meant for refreshing numpy knowledge
"""
import numpy as np

def test_arange():
    n = 1000
    a = np.arange(n)
    assert a[0] == 0
    assert a[-1] == n - 1
    print(np.sum(a))
    assert np.sum(a) == n * (n - 1)/2
import numpy as np
from spx.num import *
from spx.num.rational import *


def test_stern_brocot():
    (a, b) = (0, 1)
    (c, d) = (1, 0)
    level = 4
    dtype='int32'
    [numerators , denominators] = stern_brocot(a, b, c, d, level)
    n_true = np.array([0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1], dtype=dtype)
    d_true = np.array([1, 4, 3, 5, 2, 5, 3, 4, 1, 3, 2, 3, 1, 2, 1, 1, 0], dtype=dtype)
    print (repr(numerators))
    print (repr(denominators))
    assert np.equal(numerators, n_true).all()
    assert np.equal(denominators, d_true).all()
    assert validate_stern_brocot(a, b, c, d, numerators, denominators)

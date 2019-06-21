"""
Methods for rational numbers
"""
import numpy as np

def stern_brocot(a, b, c, d, level, dtype='int32'):
    """
    Constructs rational numbers using the Stern Brocot tree algorithm.
    Numbers are constructed in the interval [a/b , c/d]
    """
    # data type to be used for all arrays
    numerators = np.empty(2, dtype=dtype)
    denominators = np.empty(2, dtype=dtype)
    
    # left end
    numerators[0] = a
    denominators[0] = b

    # right end
    numerators[1] = c
    denominators[1] = d

    while level > 0:
        level -= 1
        old_length = numerators.size
        new_length = old_length * 2 - 1
        numerators2 = np.empty(new_length, dtype=dtype)
        denominator2 = np.empty(new_length, dtype=dtype)
        # copy data from old array
        numerators2[0::2] = numerators
        denominator2[0::2] = denominators
        # fill the middle values
        a = numerators2[0]
        b = denominator2[0]
        for i in range(1, old_length):
            j = 2*i
            c = numerators2[j]
            d = denominator2[j]
            numerators2[j-1] = a + c
            denominator2[j-1] = b + d
            # move to next
            (a, b) = (c, d)
        # rename arrays
        numerators = numerators2
        denominators = denominator2
    return (numerators, denominators)

def validate_stern_brocot(a, b, c, d, numerators, denominators):
    """
    Validates the relationship between neighboring entries
    in the Stern Brocot construction of rational numbers
    """
    # compute the constraint
    value = c * b - a * d
    if numerators.size != denominators.size:
        return False
    a = numerators[0]
    b = denominators[0]
    for i in range(1, numerators.size):
        c = numerators[i]
        d = denominators[i]
        if c * b - a * d != value:
            return False
        (a, b) = (c, d)
    return True


def print_num_den_arrays(numerators, denominators):
    """
    Prints an array of numerators
    and denominators together
    """
    for i in range(numerators.size):
        n = numerators[i]
        d = denominators[i]
        print('%d/%d ' % (n, d), end='')
    print()


"""
Numpy Extension module
"""
import numpy as np

def is_integer(x):
    """
    Checks if a numpy array contains integers
    """
    return np.equal(np.mod(x, 1), 0)



def is_bool_array(x):
    """
    Returns if this is an array of booleans
    """


def trues(size):
    """
    Create an array of Trues
    """
    return np.ones(size, dtype=bool)

def falses(size):
    """
    Create an array of Falses
    """
    return np.zeros(size, dtype=bool)
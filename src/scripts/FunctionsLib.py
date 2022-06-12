import numpy as np
from functools import cache

def random_int_array(n_low=0, n_high=1000, n_vals = 100):
    '''
        Returns a numpy random integer array in the range(n_low, n_high) with array length n_vals.
    '''
    return np.array([np.random.randint(low=n_low, high=n_high) for _ in range(n_vals)])
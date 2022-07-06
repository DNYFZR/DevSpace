import pytest, sys
sys.path.append('..')
from library.__functions import random_int_array

@pytest.mark.parametrize('test_vals', [(0, 1000, 100)])
def test_array_len(test_vals):
    assert len(random_int_array(n_low=test_vals[0], n_high=test_vals[1], n_vals=test_vals[2])) == test_vals[2]

@pytest.mark.parametrize('test_vals', [(0, 1000, 100)])
def test_bounds(test_vals):
    ret = random_int_array(n_low=test_vals[0], n_high=test_vals[1], n_vals=test_vals[2])
    assert test_vals[0] <= min(ret) and max(ret) <= test_vals[1]
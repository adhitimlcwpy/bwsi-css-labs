
import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_standard():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_max_subarray_all_negative():
    assert max_subarray_sum([-5, -2, -9]) == -2

def test_max_subarray_single_element():
    assert max_subarray_sum([4]) == 4

def test_max_subarray_empty():
    assert max_subarray_sum([]) == 0
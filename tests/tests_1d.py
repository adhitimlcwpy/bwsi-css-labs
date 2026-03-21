import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum_standard():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_negatives():
    assert two_sum([-1, -2, -3, -4], -7) == [2, 3]

def test_two_sum_zeros():
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]

def test_two_sum_no_solution():
    assert two_sum([1, 2, 3], 10) == []
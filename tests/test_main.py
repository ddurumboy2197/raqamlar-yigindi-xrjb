# test_sum.py
import pytest
from sum import sum_numbers

def test_sum_empty_list():
    assert sum_numbers([]) == 0

def test_sum_single_number():
    assert sum_numbers([5]) == 5

def test_sum_multiple_numbers():
    assert sum_numbers([1, 2, 3, 4, 5]) == 15

def test_sum_negative_numbers():
    assert sum_numbers([-1, -2, -3, -4, -5]) == -15

def test_sum_mixed_numbers():
    assert sum_numbers([1, -2, 3, -4, 5]) == 3

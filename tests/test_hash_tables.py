"""Tests for hash table related exercises."""

import pytest

from al_go_rithms.exercises.hash_tables import find_intersection_arrays


def test_intersection():
    """
    Test find_intersection_arrays with two arrays of equal length containing intersection.
    """
    arr1 = [0, 1, 2]
    arr2 = [0, 1, 3]
    res = find_intersection_arrays(arr1, arr2)

    assert res == [0, 1]


def test_no_intersection():
    """
    Test find_intersection_arrays with two arrays of equal length containing no intersection.
    """
    arr1 = [0, 1, 2]
    arr2 = [3, 4, 5]
    res = find_intersection_arrays(arr1, arr2)

    assert res

"""Exercises for hash tables."""


def find_intersection_arrays(arr1: list, arr2: list) -> list:
    """
    Find intersection between two arrays.

    Args:
        arr1 (list): First array
        arr2 (list): Second array

    Returns:
        list: Elements present in both arrays
    """

    # determine which array is largest/smallest
    if len(arr1) > len(arr2):
        large_arr = arr1
        small_arr = arr2
    else:
        large_arr = arr2
        small_arr = arr1

    # convert values in large array to dict for fast lookups
    large_arr_dict = {val: True for val in large_arr}

    # loop over small array to find values present in hash map of large array
    inter_arr = []

    for val in small_arr:
        # use get method and default value (False) to avoid KeyError
        if large_arr_dict.get(val, False):
            inter_arr.append(val)

    return inter_arr

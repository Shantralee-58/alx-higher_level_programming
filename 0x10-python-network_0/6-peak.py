#!/usr/bin/python3
"""
This module contains a function that finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)

    if n == 1:
        return list_of_integers[0]

    start, end = 0, n - 1

    while start < end:
        mid = (start + end) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return list_of_integers[start]

"""
Time Complexity: O(log(n))
"""

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
    list_of_integers.sort()
    return list_of_integers[-1]

"""
Time Complexity: O(nlog(n))
"""

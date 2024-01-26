#!/usr/bin/python3
"""Script for finding peak in list of ints using sorting.
   Time Complexity: O(n log n)
"""

def find_peak(list_of_integers):
    """Sort the list in descending order and return the first element as the peak
    """
    if not list_of_integers:
        return None

    list_of_integers.sort(reverse=True)
    return list_of_integers[0]

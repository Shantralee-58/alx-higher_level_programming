#!/usr/bin/python3
"""Script for finding peak in list of ints, interview prep
"""

def find_peak(list_of_integers):
    """Binary search implementation for finding a peak
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

# Example usage:
# peak = find_peak([1, 2, 4, 6, 3])
# print(peak)

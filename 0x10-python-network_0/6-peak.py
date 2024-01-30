#!/usr/bin/python3
""" Find the peak on unsorted list """


def find_peak(list_of_integers):
    """ Function to find the peak on unsorted list of numbers """
    if list_of_integers is None or not isinstance(list_of_integers, list):
        return None

    list_len = len(list_of_integers)

    if list_len == 0:
        return None

    # Binary search-like approach to find peak
    low, high = 0, list_len - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]

#!/usr/bin/python3
"""
Find a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers

    Args:
        list_of_integers (list): List of unsorted integers

    Returns:
        int: Peak element if found, otherwise None
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]

if __name__ == "__main__":
    # Test cases
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

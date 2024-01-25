#!/usr/bin/python3
""" Find the peak on unsorted list """


def find_peak(list_of_integers):
    """ Function to find the peak on unsorted list of numbers """
    if list_of_integers is None or not type(list_of_integers) is list:
        return None
    if len(list_of_integers) == 0:
        return None

    i = 0
    peak = list_of_integers[0]
    list_len = len(list_of_integers)

    while (i < list_len - 1):
        if i == 0 and list_of_integers[i] >= list_of_integers[i + 1]:
            peak = max(peak, list_of_integers[i])
            i += 1
        elif (list_of_integers[i] >= list_of_integers[i - 1] and
              list_of_integers[i] >= list_of_integers[i + 1]):
            peak = max(peak, list_of_integers[i])
            i += 1

        i += 1
    try:
        if list_of_integers[i] >= list_of_integers[i - 1]:
            peak = max(peak, list_of_integers[i])
    except Exception:
        pass
    return peak

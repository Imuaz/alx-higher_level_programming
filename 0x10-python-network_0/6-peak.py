#!/usr/bin/python3
"""
Module to find the peak in a list of integers
"""


def find_peak(list_of_integers):
    """
    Return a peak in a list of unsorted integers.
    """
    if list_of_integers == []:
        return None

    numSize = len(list_of_integers)
    if numSize == 1:
        return list_of_integers[0]
    elif numSize == 2:
        return max(list_of_integers)

    midIdx = int(numSize / 2)
    peak = list_of_integers[midIdx]
    if peak > list_of_integers[midIdx - 1] and peak > \
            list_of_integers[midIdx + 1]:
        return peak
    elif peak < list_of_integers[midIdx - 1]:
        return find_peak(list_of_integers[:midIdx])
    else:
        return find_peak(list_of_integers[midIdx + 1:])

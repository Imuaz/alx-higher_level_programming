#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    list_of_integers = Numbers
    size = len(Numbers)
    return Numbers[0] if size == 1 else max(Numbers) if size == 2

    midIndx = int(size / 2)
    peak = Numbers[midIdx]
    if peak > Numbers[midIdx - 1] and peak > Numbers[midIdx + 1]:
        return peak
    elif peak < Numbers[midIdx - 1]:
        return find_peak(Numbers[:midIdx])
    else:
        return find_peak(Numbers[midIdx + 1:])

#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(Numbers):
    """Return a peak in a list of unsorted integers."""
    if Numbers == []:
        return None

    size = len(Numbers)
    if size == 1:
        return Numbers[0]
    elif size == 2:
        return max(Numbers)

    mid = int(size / 2)
    peak = Numbers[mid]
    if peak > Numbers[mid - 1] and peak > Numbers[mid + 1]:
        return peak
    elif peak < Numbers[mid - 1]:
        return find_peak(Numbers[:mid])
    else:
        return find_peak(Numbers[mid + 1:])

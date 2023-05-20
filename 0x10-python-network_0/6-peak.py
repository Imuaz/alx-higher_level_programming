#!/usr/bin/python3
"""
Module to find the peak in a list of integers
"""


def find_peak(Numbers):
    """
    Return a peak in a list of unsorted integers.
    """
    if Numbers == []:
        return None

    numSize = len(Numbers)
    if numSize == 1:
        return Numbers[0]
    elif numSize == 2:
        return max(Numbers)

    midIdx = int(numSize / 2)
    peak = Numbers[midIdx]
    if peak > Numbers[midIdx - 1] and peak > Numbers[midIdx + 1]:
        return peak
    elif peak < Numbers[midIdx - 1]:
        return find_peak(Numbers[:midIdx])
    else:
        return find_peak(Numbers[midIdx + 1:])

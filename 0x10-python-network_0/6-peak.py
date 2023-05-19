#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    Get the length of the input list
    """
    length = len(list_of_integers)

    """
    Check if the list is empty
    """
    if length == 0:
        return None

    """
    Initialize the start and end indices
    """
    start = 0
    end = length - 1

    """
    Perform binary search to find a peak
    """
    while start < end:
        mid = (start + end) // 2

        """
        Check if the middle element is a peak
        """
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
    """
    Return the peak element
    """
    return list_of_integers[start]

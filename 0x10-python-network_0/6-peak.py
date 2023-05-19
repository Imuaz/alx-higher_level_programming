#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Find the peak element in a list of unsorted integers.

    Args:
        list_of_integers (List[int]): List of unsorted integers.

    Returns:
        int: Peak element in the list, or None if the list is empty.

    """
    size = len(list_of_integers)

    if size == 0:
        return None

    start = 0
    end = size - 1

    while start < end:
        mid = (start + end) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
        else:
            end = mid

    return list_of_integers[start]

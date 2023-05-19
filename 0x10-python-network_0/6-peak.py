def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (List[int]): The list of unsorted integers.

    Returns:
        int: A peak value from the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = size // 2
    peak = list_of_integers[mid]
    left_neighbor = list_of_integers[mid - 1]
    right_neighbor = list_of_integers[mid + 1]

    if peak > left_neighbor and peak > right_neighbor:
        return peak
    elif peak < left_neighbor:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])

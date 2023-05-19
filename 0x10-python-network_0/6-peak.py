def find_peak(integer_list):
    """
    Find the peak element in a list of unsorted integers.

    Args:
        integer_list (List[int]): List of unsorted integers.

    Returns:
        int: Peak element in the list.

    """
    size = len(integer_list)

    if size == 0:
        return None

    mid_index = size // 2

    if (mid_index == size - 1 or integer_list[mid_index] >=
            integer_list[mid_index + 1]) and \
            (integer_list[mid_index] >= integer_list[mid_index - 1] or
             mid_index == 0):
        return integer_list[mid_index]
    elif mid_index != size - 1 and integer_list[mid_index + 1] >
    integer_list[mid_index]:
        return find_peak(integer_list[mid_index + 1:])
    else:
        return find_peak(integer_list[:mid_index])

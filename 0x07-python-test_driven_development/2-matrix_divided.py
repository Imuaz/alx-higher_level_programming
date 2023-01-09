#!/usr/bin/python3
"""
This module contains `matrix_divided` function
Accepts:
    @matrix: a simple martix
    @div: a number to divide the elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    matrix_divided: divides a matrix by the div
    Returns: a matrix divided by the number
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")

    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix"
                            " must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    result = []
    i = 0
    for member in matrix:
        if not isinstance(member, list):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")

        result.append([])

        for n in member:
            if not isinstance(n, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

            result[i].append(round(n / div, 2))

        i += 1

    return result

#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    matrix_divided: divides all elements of a matrix
    Args:
        matrix (int, float):  list of lists of integers or floats
        div (int): divident
    Returns:
        int
    """
    size = None
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(i)
        elif size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            return [[round(j / div, 2) for j in i] for i in matrix]

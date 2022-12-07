#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda new_matrix: new_matrix ** 2, row)) for row in matrix])

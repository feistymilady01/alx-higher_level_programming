#!/usr/bin/python3
"""
Module 2-matrix_divided
Divides all element of a matrix
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """ Divides all element of a matrix by "div"
    Raises a TypeError if:
    matrix is not a list of list,
    each row of the matrix are not of same size.
    Args:
        matrix: (list) to be divided
        div: must be an int or float
        and cannot be equal to zero
    Returns a new matrix.
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for rows in matrix:
            if len(row) != len(rows):
                raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in range(len(matrix)):
        new_matrix.append(list(map(lambda y: round(y / div, 2), matrix[row])))
    return new_matrix

#!/usr/bin/python3
"""Module to divide a function"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be "
                        "a matrix (list of lists) of integers/floats")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a "
                            "matrix (list of lists) of integers/floats")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a "
                                "matrix (list of lists) of integers/floats")
    ln = len(matrix[0])
    for i in matrix:
        if len(i) > ln or len(i) < ln:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(lambda raw:
                          list(map(lambda val: round(val / div, 2),
                                   raw)), matrix))
    return new_matrix

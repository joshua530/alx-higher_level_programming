#!/usr/bin/python3

"""
This module contains a matrix division function
"""


def matrix_divided(matrix, div):
    """
    Divides numbers in a matrix by a divisor

    Args:
        matrix: a list of lists containing numbers
        div: number to divide each of the items in the matrix with

    Returns:
        a matrix that contains all its numbers divided by the provided divisor

    Raises:
        ZeroDivisionError: if div is zero
        TypeError: if matrix is not a list of lists
        TypeError: if div is not a float or integer
        TypeError: if matrix contains a value that is not a number
        TypeError: if matrix contains lists that are not of the same length
    """
    if type(matrix) not in [list]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")

    new_matrix = []
    row_len = -1

    for row in matrix:
        # we're on the first row so we don't know the row size
        if row_len == -1:
            row_len = len(row)
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        tmp = []
        for num in row:
            if type(num) not in [float, int]:
                raise TypeError(
                    "matrix must be a matrix (list of lists)\
                        of integers/floats")
            tmp.append(round(num / div, 2))
        new_matrix.append(tmp)
    return new_matrix

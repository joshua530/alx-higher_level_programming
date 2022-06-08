#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """computes square values of all integers of a matrix

    Args:
        matrix: the matrix whose squares are to be computed

    Returns:
        matrix with computed squares
    """
    squares = []

    for arr in matrix:
        squares.append([num * num for num in arr])
    return squares

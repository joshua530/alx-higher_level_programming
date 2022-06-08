#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    """squares a matrix's values using the map method

    the returned matrix is different from the one passed
    into the function

    Args:
        matrix: the matrix to square

    Returns:
        the square matrix"""
    squared = []

    for num_list in matrix:
        squared.append(list(map(lambda x: x*x, num_list)))

    return squared

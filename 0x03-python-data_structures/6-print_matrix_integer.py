#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """prints out a matrix made up of integers

    Args:
        matrix: the matrix to be printed out

    Returns:
        None
    """
    for arr in matrix:
        for i in range(len(arr)):
            if i == len(arr) - 1:
                print("{:d}".format(arr[i]))
            else:
                print("{:d} ".format(arr[i]), end="")

#!/usr/bin/python3
"""This module contains Pascal's triangle implementation"""


def pascal_triangle(n):
    """Creates a pascal's triangle representation

    Args:
        n: the nth iteration of the triangle

    Returns:
        a list containing Pascal's triangle for n
    """
    pascal = []
    for i in range(n):
        if i == 0:
            pascal.append([1])
        elif i == 1:
            pascal.append([1, 1])
        else:
            tmp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(pascal[i - 1][j] + pascal[i - 1][j - 1])
            pascal.append(tmp)
    return pascal

#!/usr/bin/python3
"""
Defines matrix multiplication method
"""


def matrix_mul(m_a, m_b):
    """
    multiplies two matrices
    """
    if type(m_a) not in [list]:
        raise TypeError("m_a must be a list")
    if type(m_b) not in [list]:
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or len(m_b) == 0 or m_a == [[]] or m_b == [[]]:
        raise ValueError("{} can't be empty".format("m_a" if len(m_a) == 0 else "m_b"))

    for row in m_a:
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must should be of the same size")
        if len(row) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

    for row in m_b:
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must should be of the same size")

    l = []
    new_matrix = []
    n = 0
    for row in range(len(m_a)):
        l = []
        for colB in range(len(m_b[0])):
            for i in range(len(m_a[0])):
                n += m_a[row][i] * m_b[i][colB]
            l.append(n)
            n = 0
        new_matrix.append(l)

    return new_matrix

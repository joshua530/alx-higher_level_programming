#!/usr/bin/python3
"""
Contains function for multiplying matrices using numpy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies matrices and returns the result"""
    return numpy.matmul(m_a, m_b)

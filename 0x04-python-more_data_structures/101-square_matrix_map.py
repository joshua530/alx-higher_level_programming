#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda num_list: list(map(lambda num: num * num, num_list)), matrix))

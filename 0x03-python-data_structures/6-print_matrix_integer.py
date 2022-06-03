#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for i in range(len(arr)):
            if i == len(arr) - 1:
                print("{}".format(arr[i]))
            else:
                print("{} ".format(arr[i]), end="")

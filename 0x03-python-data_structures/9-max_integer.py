#!/usr/bin/python3


def max_integer(my_list=[]):
    max_int = None
    if len(my_list) == 0:
        return max_int

    for i in my_list:
        if max_int is None or i > max_int:
            max_int = i
    return max_int

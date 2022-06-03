#!/usr/bin/python3


def new_in_list(my_list: list, idx: int, element: int):
    tmp = my_list.copy()
    if len(my_list) == 0 or idx < 0 or idx >= len(my_list):
        return tmp
    tmp[idx] = element
    return tmp

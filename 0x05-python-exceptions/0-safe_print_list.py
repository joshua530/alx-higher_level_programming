#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        return my_list[x]
    except Exception:
        return my_list[len(my_list) - 1]

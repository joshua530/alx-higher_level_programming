#!/usr/bin/python3


def uniq_add(my_list=[]):
    """adds all unique integers in a list

    Args:
        my_list: the list whose integers are to be added

    Returns:
        the calculated sum
    """
    unique_ints = set(my_list)
    the_sum = sum(unique_ints)
    return the_sum

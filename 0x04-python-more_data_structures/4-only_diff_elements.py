#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """finds element[s] present in one set but not in the other

    Args:
        set_1: first set
        set_2: second set

    Returns:
        set of elements present in only one of the lists"""
    unique = {}
    unique_set = set()
    for element in set_1:
        if element not in unique.keys():
            unique[element] = 1
        else:
            unique[element] += 1
    for element in set_2:
        if element not in unique.keys():
            unique[element] = 1
        else:
            unique[element] += 1

    for k, v in unique.items():
        if v == 1:
            unique_set.add(k)
    return unique_set

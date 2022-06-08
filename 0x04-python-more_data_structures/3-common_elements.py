#!/usr/bin/python3


def common_elements(set_1, set_2):
    """finds common elements between two sets

    Args:
        set_1: first set
        set_2: second set

    Returns:
        a set comprised of the common elements"""
    common = [x for x in set_1 for z in set_2 if x == z]
    return set(common)

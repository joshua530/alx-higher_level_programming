#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """multiplies dictionary values by 2

    Args:
        a_dictionary: dictionary whose values are to be multiplied by 2

    Returns:
        new dictionary whose values are twice of the original one
    """
    new_dict = {}

    for key, val in a_dictionary.items():
        new_dict[key] = val * 2

    return new_dict

#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary: dict):
    """prints a dictionary using its sorted keys

    Args:
        a_dictionary: the dictionary to print out

    Returns:
        None
    """
    keys = sorted(list(a_dictionary.keys()))
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))

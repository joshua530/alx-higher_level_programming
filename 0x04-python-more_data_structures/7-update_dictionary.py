#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """updates or adds a key if it doesn't exist

    Args:
        key: the key to add or update
        value: value of the key

    Returns:
        updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary

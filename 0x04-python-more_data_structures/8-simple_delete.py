#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """deletes a dictionary key

    Args:
        a_dictionary: dictionary whose key is to be removed
        key: the key to remove

    Returns:
        the modified dictionary
    """
    a_dictionary.pop(key, None)
    return a_dictionary

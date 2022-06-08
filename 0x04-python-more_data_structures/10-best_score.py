#!/usr/bin/python3


def best_score(a_dictionary):
    """returns key with highest integer value

    Args:
        a_dictionary: the dictionary whose highest integer value is to be found

    Return:
        key with highest integer value or None if no score was found
    """
    if a_dictionary is None or len(a_dictionary.keys()) == 0:
        return None

    max_key = None
    for key, val in a_dictionary.items():
        if max_key is None or val > a_dictionary[max_key]:
            max_key = key

    return max_key

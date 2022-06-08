#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """deletes key which maps to a certain value from dictionary

    Args:
        a_dictionary: the dictionary to modify
        value: value whose key[s] are to be deleted

    Returns:
        dictionary whose keys that map to value have been deleted
    """
    to_delete = []
    for k, v in a_dictionary.items():
        if v == value:
            to_delete.append(k)
    for key in to_delete:
        a_dictionary.pop(key)
    return a_dictionary

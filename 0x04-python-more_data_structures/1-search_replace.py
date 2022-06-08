#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """searches and replaces an element in a list

    Args:
        my_list: list to search for element in
        search: item to be replaced
        replace: item to replace with

    Returns:
        list with all instances of item replaced
    """
    new_list = []

    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

    return new_list

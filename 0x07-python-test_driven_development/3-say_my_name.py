#!/usr/bin/python3

"""
Contains function that prints one's name
"""

def say_my_name(first_name, last_name=""):
    """
    Prints out full name

    Args:
        first_name: the first name
        last_name: the last name

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")

    print(f"{first_name} {last_name}")

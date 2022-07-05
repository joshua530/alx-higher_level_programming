#!/usr/bin/python3
"""Contains function that serializes an object to simple data
structures
"""


def class_to_json(obj):
    """Serializes an object to simple data structures

    The serialization is done to both the object and it's properties
    Object becomes a dictionary with the properties being keys and their
    values being the corresponding object's property's value
    """
    return obj.__dict__

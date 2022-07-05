#!/usr/bin/python3
"""Contains function that returns json representation of an object"""


def to_json_string(my_obj):
    """Returns json representation of my_obj"""
    json = __import__("json")
    return json.dumps(my_obj)

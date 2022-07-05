#!/usr/bin/python3
"""Contains function that onverts json string to object"""


def from_json_string(my_str):
    """Converts json string to object"""
    import json

    return json.loads(my_str)

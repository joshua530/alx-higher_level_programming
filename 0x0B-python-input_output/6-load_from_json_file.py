#!/usr/bin/python3
"""Contains function that loads json object from a file"""


def load_from_json_file(filename):
    """Loads json object from a file and returns it

    Args:
        filename: file to load json string from
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)

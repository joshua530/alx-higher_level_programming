#!/usr/bin/python3
"""Contains function that writes JSON object to a file"""


def save_to_json_file(my_obj, filename):
    """Writes JSON object to a file"""
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)

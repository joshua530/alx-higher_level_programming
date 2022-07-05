#!/usr/bin/python3
"""Contains function that appends text to a file"""


def append_write(filename="", text=""):
    """Appends text to a file and returns length
    of appended text
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)

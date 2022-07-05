#!/usr/bin/python3
"""Defines function that appends line to file that matches a given keyword"""


def append_after(filename="", search_string="", new_string=""):
    """Appends string to every line in a file that contains keyword

    Args:
        search_string: the string to look for
        new_string: string to append to lines that match
    """

    with open(filename, mode="r+", encoding="utf-8") as f:
        tmp = ""
        for line in f:
            tmp += line
            if search_string in line:
                tmp += new_string
        f.seek(0)
        f.write(tmp)

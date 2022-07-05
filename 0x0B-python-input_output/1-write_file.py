#!/usr/bin/python3
"""Contains function that writes text to a file"""


def write_file(filename="", text=""):
    """writes text to a file and returns the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)

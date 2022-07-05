#!/usr/bin/python3
"""Contains file reading function"""


def read_file(filename=""):
    """Reads UTF-8 file and prints it's contents to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

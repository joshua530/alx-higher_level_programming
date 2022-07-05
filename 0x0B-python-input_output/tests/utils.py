#!/usr/bin/python3

import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def get_file_path(filename):
    """Finds absolute file path"""
    return CURRENT_DIR + "/" + filename

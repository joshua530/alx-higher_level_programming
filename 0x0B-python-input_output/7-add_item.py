#!/usr/bin/python3
"""Script that fetches command line arguments and saves them to a file

If the file does not exist, it is created. If it exists, the
content is appended to it(in JSON form)
"""

import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
cmd_line_args = sys.argv[1:]

try:
    file_contents = load_from_json_file("add_item.json")
except FileNotFoundError:
    file_contents = []

file_contents = file_contents + cmd_line_args
save_to_json_file(file_contents, "add_item.json")

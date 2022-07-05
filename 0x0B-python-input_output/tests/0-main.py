#!/usr/bin/python3
import os


read_file = __import__('0-read_file').read_file

file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "my_file_0.txt")

read_file(file)

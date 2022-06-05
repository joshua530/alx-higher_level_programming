#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    size = len(argv)
    end_clause = "arguments:"
    if size == 2:
        end_clause = "argument:"
    elif size == 1:
        end_clause = "arguments."

    print("{} {}".format(size - 1, end_clause))

    for i in range(1, size):
        print("{}: {}".format(i, argv[i]))

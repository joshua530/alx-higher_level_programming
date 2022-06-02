#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    size = len(argv)
    total = 0

    for i in range(1, size):
        total += int(argv[i])
    print(total)

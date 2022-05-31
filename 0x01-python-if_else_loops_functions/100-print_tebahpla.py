#!/usr/bin/python3
def get_char(i):
    if i % 2 == 0:
        return chr(i)
    return chr(i - 32)


for i in range(122, 96, -1):
    print("{:s}".format(get_char(i)), end="")

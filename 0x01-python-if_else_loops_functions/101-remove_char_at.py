#!/usr/bin/python3
def remove_char_at(str, n):
    size = len(str)
    if n > size - 1:  # n is out of bounds
        return str
    tmp = ""
    to_skip = n
    # if n < 0:
    #     to_skip = size + n
    for i in range(size):
        if i != to_skip:
            tmp += str[i]
    return tmp

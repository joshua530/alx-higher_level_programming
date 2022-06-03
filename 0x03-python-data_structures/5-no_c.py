#!/usr/bin/python3


def no_c(my_string):
    tmp = []
    for c in my_string:
        if c != "c" and c != "C":
            tmp.append(c)
    return "".join(tmp)

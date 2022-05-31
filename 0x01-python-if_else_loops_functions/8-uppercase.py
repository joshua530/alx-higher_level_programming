#!/usr/bin/python3
def uppercase(str):
    to_print = ""
    for i in range(len(str)):
        ascii = ord(str[i])
        if ascii >= 65 and ascii <= 90:  # uppercase already
            to_print += str[i]
        elif ascii >= 97 and ascii <= 122:  # lowercase, convert to uppercase
            to_print += chr(ord(str[i]) - 32)
        else:  # other characters
            to_print += str[i]
    print("{:s}".format(to_print))

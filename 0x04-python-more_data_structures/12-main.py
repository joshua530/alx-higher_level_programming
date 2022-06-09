#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__("12-roman_to_int").roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMMMM"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DUCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CXXIV"
print("{} = {}".format(roman_number, roman_to_int(roman_number))) # 124

roman_number = "XCIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number))) # 99

roman_number = "LXXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number))) # 89

roman_number = ""
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = None
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

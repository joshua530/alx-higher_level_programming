#!/usr/bin/python3


def roman_to_int(roman_string):
    """converts a roman numeral to an integer

    Numbers:
    I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
    Restrictions: 0 <= number <= 3999

    Returns:
        the converted roman number or zero if conversion failed
    """
    if (
        roman_string is None
        or roman_string.__class__.__name__ != "str"
        or len(roman_string) == 0
    ):
        return 0
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    for char in roman_string:
        int_val = roman_numerals[char]
        if sum < int_val:
            sum = int_val - sum
        else:
            sum += int_val
    return sum

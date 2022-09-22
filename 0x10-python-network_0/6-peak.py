#!/usr/bin/python3
"""
Contains function that finds the peak in a given list of numbers
"""


def find_peak(list_of_integers):
    """Finds the peak in a given list of integers

    Peak: a number n in the list where n is greater than each of it's neighbours
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid = len(list_of_integers) // 2
    left = 0
    right = len(list_of_integers) - 1
    l_ints = list_of_integers

    if l_ints[0] > l_ints[1]:
        return l_ints[0]
    if l_ints[right] > l_ints[right - 1]:
        return l_ints[right]

    while left <= mid:
        left += 1
        right -= 1

        if l_ints[left] >= l_ints[left - 1] and l_ints[left] >= l_ints[left + 1]:
            return l_ints[left]
        if l_ints[right] >= l_ints[right + 1] and l_ints[right] >= l_ints[right - 1]:
            return l_ints[right]
    return None

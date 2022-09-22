#!/usr/bin/python3
"""
Contains function that finds the peak in a given list of numbers
"""


def find_peak(list_of_integers):
    """Finds the peak in a given list of integers

    Peak: a number n in the list where n is greater than each of
    it's neighbours
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid = len(list_of_integers) // 2
    left = 0
    right = len(list_of_integers) - 1
    l_i = list_of_integers

    if l_i[0] > l_i[1]:
        return l_i[0]
    if l_i[right] > l_i[right - 1]:
        return l_i[right]

    while left <= mid:
        left += 1
        right -= 1

        if l_i[left] >= l_i[left - 1] and l_i[left] >= l_i[left + 1]:
            return l_i[left]
        if l_i[right] >= l_i[right + 1] and l_i[right] >= l_i[right - 1]:
            return l_i[right]
    return None

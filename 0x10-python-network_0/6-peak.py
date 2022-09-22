#!/usr/bin/python3
"""
Contains function that finds the peak in a given list of numbers
"""


def find_peak(list_of_integers):
    """Finds the peak in a given list of integers
    """
    if len(list_of_integers) == 0:
        return None

    # O(nlog(n)) time complexity
    sorted_l = sort_list(list_of_integers)
    # O(k)
    return sorted_l[len(sorted_l) - 1]


def sort_list(list_of_integers):
    """Sorts a given list of integers"""
    if len(list_of_integers) == 1 or len(list_of_integers) == 0:
        return list_of_integers

    mid = int(len(list_of_integers) / 2)
    left = sort_list(list_of_integers[:mid])
    right = sort_list(list_of_integers[mid:])

    i_left = 0
    i_right = 0
    sorted_l = []
    while i_left < len(left) and i_right < len(right):
        if left[i_left] < right[i_right]:
            sorted_l.append(left[i_left])
            i_left += 1
        else:
            sorted_l.append(right[i_right])
            i_right += 1

    # add any left over numbers in either of the lists to the sorted list
    for i in range(i_left, len(left)):
        sorted_l.append(left[i])
    for i in range(i_right, len(right)):
        sorted_l.append(right[i])

    return sorted_l

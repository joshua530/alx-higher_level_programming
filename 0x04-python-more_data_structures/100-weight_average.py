#!/usr/bin/python3


def weight_average(my_list=[]):
    """calculates weighted average

    Args:
        my_list: the list whose weighted average we are finding

    Returns:
        weighted average or 0 if calculation failed
    """
    numerator = 0
    denominator = 0
    for num_set in my_list:
        numerator += num_set[0] * num_set[1]
        denominator += num_set[1]
    if denominator == 0:
        return 0
    return numerator / denominator

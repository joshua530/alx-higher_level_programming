#!/usr/bin/python3
"""
Contains class that restricts creation of instance attributes
"""


class LockedClass:
    """
    Restricts dynamic creation of instance attributes

    Only first_name is allowed
    """
    
    __slots__ = "first_name"

#!/usr/bin/python3
from typing import Type


def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result = {}".format(result))
    return result

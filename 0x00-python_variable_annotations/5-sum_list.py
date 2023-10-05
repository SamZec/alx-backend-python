#!/usr/bin/ev python3
"""5-sum_list.py - module for a type-annotated function sum_list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        takes a list input_list of floats as argument
        returns their sum as a float
    """
    sum_float = 0.0

    for item in input_list:
        sum_float += item

    return sum_float

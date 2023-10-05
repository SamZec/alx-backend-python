#!/usr/bin/env python3
"""6-sum_mixed_list.py - module for type-annotated function sum_mixed_list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        takes a list mxd_lst of integers and floats
        returns their sum as a float
    """
    sum_mxd_list = 0.0

    for item in mxd_lst:
        sum_mxd_list += item

    return sum_mxd_list

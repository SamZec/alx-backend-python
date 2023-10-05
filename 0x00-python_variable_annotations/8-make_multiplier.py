#!/usr/bin/env python3
"""
    8-make_multiplier.py - module for type-annotated function make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        takes a float multiplier as argument
        returns a function that multiplies a float by multiplier.
    """
    def mult(num: float) -> float:
        return multiplier * num
    return mult

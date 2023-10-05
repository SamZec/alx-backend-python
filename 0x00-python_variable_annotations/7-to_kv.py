#!/usr/bin/env python3
"""7-to_kv.py - module for type-annotated function to_kv"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        takes a string k and an int OR float v as arguments
        returns a tuple. The first element of the tuple is the string k.
        The second element is the square of the int/float v
    """
    annot_tuple: Tuple[str, float] = (k, v**2)

    return annot_tuple

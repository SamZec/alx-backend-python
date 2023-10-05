#!/usr/bin/env python3
"""100-safe_first_element.py - Duck typing for first element of a sequence"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """correct duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None

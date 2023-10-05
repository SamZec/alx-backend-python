#!/usr/bin/env python3
"""9-element_length.py - module for duck typing"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return values with the appropriate annotated types"""
    return [(i, len(i)) for i in lst]

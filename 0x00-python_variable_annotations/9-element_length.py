#!/usr/bin/env python3
"""
Returns a list of tuples with each element and its length
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotates function’s parameters
    return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]

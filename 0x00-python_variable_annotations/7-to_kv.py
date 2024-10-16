#!/usr/bin/env python3
"""
Returns a tuple with a string and the square of an int or float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function to_kv that takes
    string k and an int OR float v as arguments
    returns a tuple
    """
    return (k, float(v ** 2))

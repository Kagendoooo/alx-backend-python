#!/usr/bin/env python3
"""
Returns a function that multiplies a float by the given multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function make_multiplier that takes
    a float multiplier as argument
    returns a function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier

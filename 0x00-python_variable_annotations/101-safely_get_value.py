#!/usr/bin/env python3
"""
Safely gets a value from a dictionary
returning a default if the key is not found
"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Given the parameters and the return values
    add type annotations to the function
    """
    if key in dct:
        return dct[key]
    else:
        return default

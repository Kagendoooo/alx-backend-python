#!/usr/bin/env python3
"""
Safely gets a value from a dictionary
returning a default if the key is not found
"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, 
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary, returning a default if the key is not found.

    Parameters:
    dct (Mapping[Any, Any]): The dictionary to retrieve the value from.
    key (Any): The key to look for in the dictionary.
    default (Union[T, None]): The default value to return if the key is not found.

    Returns:
    Union[Any, T]: The value from the dictionary or the default.
    """
    if key in dct:
        return dct[key]
    else:
        return default

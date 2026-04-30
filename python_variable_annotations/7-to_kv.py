#!/usr/bin/env python3
"""
This module provides a function that converts a string and number to a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the string k and the square of v.

    Args:
        k (str): The string element.
        v (int | float): The number to be squared.

    Returns:
        tuple: A tuple containing the string and the float square of v.
    """
    return (k, float(v ** 2))

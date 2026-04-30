#!/usr/bin/env python3
"""
This module provides a function that returns another function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable: A function that takes a float and returns a float.
    """
    def multiplier_func(n: float) -> float:
        """Multiplies a float by the outer multiplier."""
        return n * multiplier

    return multiplier_func

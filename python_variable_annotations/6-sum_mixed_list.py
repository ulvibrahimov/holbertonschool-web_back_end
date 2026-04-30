#!/usr/bin/env python3
"""
This module provides a function to sum a list of both integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list containing both integers and floats.

    Args:
        mxd_lst (list): A list of integers and floats.

    Returns:
        float: The sum of the list elements as a float.
    """
    return float(sum(mxd_lst))

#!/usr/bin/env python3
"""
This module provides a function to calculate the length of items in an iterable.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of elements within an iterable.

    Args:
        lst (Iterable): An iterable of sequences.

    Returns:
        List: A list of tuples, each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]

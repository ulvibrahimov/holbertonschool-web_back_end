#!/usr/bin/env python3
"""
Module to measure runtime of concurrent coroutines.
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n and returns time per task.

    Args:
        n (int): The number of coroutines launched.
        max_delay (int): The max delay parameter.

    Returns:
        float: Average execution time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    
    return (end_time - start_time) / n

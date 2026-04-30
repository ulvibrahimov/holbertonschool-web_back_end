#!/usr/bin/env python3
"""
Module to measure the runtime of parallel asynchronous comprehensions.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using
    asyncio.gather and measures the total runtime.
    
    Returns:
        The total runtime as a float.
    """
    start_time = time.perf_counter()
    
    # Run async_comprehension 4 times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    
    end_time = time.perf_counter()
    
    return end_time - start_time

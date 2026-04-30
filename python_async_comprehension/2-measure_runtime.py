#!/usr/bin/env python3
"""
Module to measure the runtime of four parallel async comprehensions.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using
    asyncio.gather and measures the total execution time.
    """
    start_time = time.perf_counter()
    
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    
    end_time = time.perf_counter()
    
    return end_time - start_time

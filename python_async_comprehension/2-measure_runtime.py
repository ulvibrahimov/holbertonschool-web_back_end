#!/usr/bin/env python3
"""
This module contains a coroutine that measures the total execution time
of running multiple asynchronous comprehensions concurrently.
It utilizes the asyncio.gather method to run tasks in parallel.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes the async_comprehension coroutine four times in parallel
    using asyncio.gather and returns the total runtime elapsed during
    the execution of all four coroutines.
    """
    start_time = time.perf_counter()
    
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end_time = time.perf_counter()
    return end_time - start_time

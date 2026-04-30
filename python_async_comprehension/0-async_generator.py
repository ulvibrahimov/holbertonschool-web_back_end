#!/usr/bin/env python3
"""
This module provides an asynchronous generator function.
The function is designed to yield random floating-point numbers
after a specified asynchronous delay to demonstrate async generators.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    A coroutine that loops exactly 10 times. During each iteration,
    it asynchronously waits for 1 second, and then yields a random
    floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

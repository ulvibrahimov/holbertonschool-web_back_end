#!/usr/bin/env python3
"""
This module defines an asynchronous generator coroutine that yields random
floating-point numbers. It demonstrates the use of the asyncio and random
modules to create a non-blocking stream of data over a period of time.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yields a random number between 0 and 10 every second
    for a total of ten iterations. This coroutine uses asyncio.sleep to
    ensure the wait is non-blocking and random.uniform for the values.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


#!/usr/bin/env python3
"""
This module contains an asynchronous generator coroutine that yields
random floating-point numbers after an asynchronous delay.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that loops ten times, waiting one second
    between each iteration before yielding a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

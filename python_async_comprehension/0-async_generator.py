#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields random numbers.
The generator loops ten times and waits one second between each yield.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yields a random float between 0 and 10 ten times.
    Each yield is preceded by an asynchronous wait of one second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

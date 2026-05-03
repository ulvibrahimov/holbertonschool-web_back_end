#!/usr/bin/env python3
"""This module provides a coroutine that yields random numbers asynchronously."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops ten times, waits one second each time, and yields a random float."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

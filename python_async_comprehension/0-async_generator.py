#!/usr/bin/env python3
"""This module contains an asynchronous generator coroutine that yields random numbers."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """This coroutine loops 10 times, waits 1 second asynchronously, and yields a random float."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

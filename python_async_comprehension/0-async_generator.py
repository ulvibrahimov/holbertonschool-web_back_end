#!/usr/bin/env python3
"""
Module that contains an asynchronous generator coroutine.
"""
import asyncio
import random
import typing


async def async_generator() -> typing.AsyncGenerator[float, None]:
    """
    Coroutine that loops 10 times, each time asynchronously waiting
    1 second, then yields a random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

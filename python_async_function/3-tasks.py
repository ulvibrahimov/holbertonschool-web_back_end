#!/usr/bin/env python3
"""
Module for creating asyncio tasks from coroutines.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay limit.

    Returns:
        asyncio.Task: The task object created.
    """
    return asyncio.create_task(wait_random(max_delay))

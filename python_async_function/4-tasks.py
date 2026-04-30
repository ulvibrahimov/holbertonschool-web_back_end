#!/usr/bin/env python3
"""
This module provides a coroutine that spawns multiple asyncio tasks
concurrently and returns their delays in ascending order.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns the list of completed delays in ascending order.

    Args:
        n (int): The number of times to spawn the task.
        max_delay (int): The maximum delay limit for each task.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
        
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
        
    return delays

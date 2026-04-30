#!/usr/bin/env python3
"""
Module for concurrently running asyncio tasks.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times and returns the delays.

    Args:
        n (int): The number of times to spawn the task.
        max_delay (int): The maximum delay limit.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
        
    return delays

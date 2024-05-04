#!/usr/bin/env python3
"""The basics of async"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 1) -> List[float]:
    """basic async"""
    delays: List[float] = []
    for i in range(n):
        delays.append(await task_wait_random(max_delay))
    return sorted(delays)

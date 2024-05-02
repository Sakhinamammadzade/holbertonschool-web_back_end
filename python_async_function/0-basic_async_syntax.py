#!/usr/bin/env python3
"""The basics of async"""
import random
import asyncio


async def wait_random(max_delay=10):
    """basic async"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

asyncio.run(wait_random())

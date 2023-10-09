#!/usr/bin/env python3
"""4-tasks.py - module for an async routine called task_wait_n"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """an async routine function returning list of delays"""
    delays = await asyncio.gather(*(task_wait_random(max_delay)
                                  for i in range(n)))
    return sorted(delays)

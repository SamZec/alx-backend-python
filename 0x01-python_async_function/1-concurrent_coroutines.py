#!/usr/bin/env python3
"""1-concurrent_coroutines.py - module for an async routine called wait_n"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """an async routine function returning list of delays"""
    delays = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(delays)

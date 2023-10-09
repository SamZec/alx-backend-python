#!/usr/bin/env python3
"""1-concurrent_coroutines.py - module for an async routine called wait_n"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """an async routine function returning list of delays"""
    return await asyncio.gather(*(wait_random(max_delay) for i in range(n)))

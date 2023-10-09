#!/usr/bin/env python3
"""0-basic_async_syntax.py - module for wait_random function"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine function"""
    res = await asyncio.sleep(0, random.uniform(0, max_delay))
    return res


if __name__ == "__main__":
    wait_random()

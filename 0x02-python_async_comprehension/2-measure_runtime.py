#!/usr/bin/env python3
"""2-measure_runtime.py - module for measure_runtime coroutine"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ execute async_comprehension four times in parallel using
        asyncio.gather, measure the total runtime and return it.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension(), async_comprehension(),
                           async_comprehension(), async_comprehension()))
    total_time = time.time() - start

    return total_time

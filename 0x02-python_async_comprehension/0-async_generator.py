#!/usr/bin/env python3
"""0-async_generator.py - module for async_generator function"""

import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """
        coroutine that loop 10 times and asynchronously wait 1 second
        yield a random number between 0 and 10.
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)

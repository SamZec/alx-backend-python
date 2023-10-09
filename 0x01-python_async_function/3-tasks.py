#!/usr/bin/env python3
"""3-tasks.py - module for task_wait_random function"""

import asyncio
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable:
    """returns an asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))

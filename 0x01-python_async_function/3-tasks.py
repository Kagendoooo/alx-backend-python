#!/usr/bin/env python3
"""
Task that spawns wait_random with max_delay and returns asyncio.Task.
"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task.
    The task runs wait_random with the given max_delay.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random

    return asyncio.create_task(wait_random(max_delay))

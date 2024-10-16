#!/usr/bin/env python3
"""
Measure the runtime of async_comprehension.
"""
import asyncio
import time
from 1_async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """Measures the total runtime of executing async_comprehension four times."""
    start_time = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = time.time()
    return end_time - start_time

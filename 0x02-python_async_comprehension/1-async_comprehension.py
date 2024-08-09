#!/usr/bin/env python3
'''
1. Async Comprehensions
'''

async_generator = __import__('0-async_generator').async_generator
import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    '''
    takes no arguments. The coroutine will collect 10 random numbers
    using an async comprehensing over async_generator, then return the
    10 random numbers.
    '''
    return [task async for task in async_generator()]

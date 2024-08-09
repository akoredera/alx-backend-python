#!/usr/bin/env python3
'''
0. The basics of async
'''
import asyncio
import random


async def wait_random(max_delay: int = 10):
    '''
    asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random
    that waits for a random delay between 0 and max_delay
    '''
    ranVal = random.uniform(0, max_delay)
    waitVal = await asyncio.sleep(ranVal)
    return ranVal

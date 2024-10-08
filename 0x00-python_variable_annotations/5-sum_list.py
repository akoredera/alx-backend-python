#!/usr/bin/env python3
'''
type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float.
'''
import functools
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''sum_list function'''
    return functools.reduce(lambda a, b: a + b, input_list)

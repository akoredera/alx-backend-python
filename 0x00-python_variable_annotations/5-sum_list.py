#!/usr/bin/env python3
import functools
from typing import List
'''
type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float.
'''
#type Value = list[float]
def sum_list(input_list: List[float]) -> float:
    return functools.reduce(lambda a, b: a + b, input_list)

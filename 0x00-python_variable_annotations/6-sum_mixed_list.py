#!/usr/bin/env python3
'''
type-annotated function sum_mixed_list which takes
a list mxd_lst of integers and floats and returns their sum as a float
'''
import functools
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''sum_list function'''
    return functools.reduce(lambda a, b: a + b, mxd_list)

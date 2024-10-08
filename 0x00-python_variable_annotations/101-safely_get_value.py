#!/usr/bin/env python3
'''
Given the parameters and the return values,
add type annotations to the function
'''
from typing import Any, Union, TypeVar, Mapping
T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    '''safety get value'''
    if key in dct:
        return dct[key]
    else:
        return default

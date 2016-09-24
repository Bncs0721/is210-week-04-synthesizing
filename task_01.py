#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module creates fahrenheit_to_celsius."""

import decimal

def fahrenheit_to_celsius(degrees):
    """Converts fahrenheit degrees to celsius.

    Arg:
        degrees(int, float):Degrees in F to be converted to C.

    Returns:
        Decimal:Degrees in C.

    Example:

        >>> fahrenheit_to_celsius(212)
        Decimal('100')
        
    >>> fahrenheit_to_celsius(104.5)
    Decimal('40.27777777777777777777777778')
    """
    answer = ((decimal.Decimal(degrees - 32)) * 5)/9
    return answer

    print answer

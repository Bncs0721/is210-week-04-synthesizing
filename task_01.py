#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module creates fahrenheit_to_celsius."""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Converts fahrenheit degrees to celsius.

    Arg:
        degrees(int, float):Degrees in F to be converted to C.

    Returns:
        Decimal:Degrees in Celsius.

    Example:

        >>> fahrenheit_to_celsius(212)
        Decimal('100')
        
        >>> fahrenheit_to_celsius(104.5)
        Decimal('40.27777777777777777777777778')
    """
    answer = ((decimal.Decimal(degrees - 32)) * 5)/9
    return answer


def celsius_to_kelvin(degrees):
    """Converts celsius to kelvin.

    Arg:
        degrees(int, float):Degrees in C to be converted to K.

    Retunrs:
        Decimal:Degrees in Kelvin.

    Example:

        >>> celsius_to_kelvin(100)
        Decimal('373.15')
        
        >>> celsius_to_kelvin(150)
        Decimal('423.15')

    """
    answer = ABSOLUTE_DIFFERENCE + degrees
    return answer


def fahrenheit_to_kelvin(degrees):
    """Converts fahrenheit to kelvin.

    Arg:
        degrees(int, float):Degrees in F to be converted to K.

    Returns:
        Decimal:Degrees in kelvin.

    Example:

        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')
        
    >>> fahrenheit_to_kelvin(200)
    Decimal('366.4833333333333333333333333')
    """
    answer = (fahrenheit_to_celsius(degrees)) + ABSOLUTE_DIFFERENCE
    return answer

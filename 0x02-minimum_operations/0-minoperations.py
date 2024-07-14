#!/usr/bin/python3
"""Minimum Operations"""
from math import isqrt


def factors(n):
    """
    Calculates the factors of a given number.

    Parameters:
        n (int): The number for which factors need
        to be calculated.

    Returns:
        list: A list of factors of the given number.
    """
    mylist = []
    while n % 2 == 0:
        mylist.append(2)
        n //= 2
    for i in range(3, isqrt(n) + 1, 2):
        while n % i == 0:
            mylist.append(i)
            n //= i
    if n > 2:
        mylist.append(n)
    return mylist


def minOperations(n):
    """
    Calculates the minimum number of operations required to
    transform a given number into 1.

    Parameters:
    n (int): The number to be transformed.

    Returns:
    int: The minimum number of operations required.
    """
    if not isinstance(n, int) or n < 2:
        return 0
    else:
        numOperations = sum(factors(n))
        return int(numOperations)

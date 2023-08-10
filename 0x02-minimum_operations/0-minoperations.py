#!/usr/bin/env python3
"""
Operations module
"""


def minOperations(n):
    """
    a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required to achieve
        'n' H characters.
             Returns 0 if 'n' is impossible to achieve.
    """
    if n <= 1:
        return 0

    opResult = 0
    factor = 2

    while factor <= n:
        if n % factor == 0:
            opResult += factor
            n /= factor
        else:
            factor += 1

    return opResult

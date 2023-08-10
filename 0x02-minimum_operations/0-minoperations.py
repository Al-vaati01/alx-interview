#!/usr/bin/python3
"""
Operations module
"""


def minOperations(n):
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

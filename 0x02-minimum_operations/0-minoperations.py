#!/usr/bin/env python3
def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly 'n' H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required to achieve
        'n' H characters.
             Returns 0 if 'n' is impossible to achieve.
    """
    if n <= 1:
        return 0

    result = 0

    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            result += i
            n //= i

    if n > 1:
        result += n

    return result

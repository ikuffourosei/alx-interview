#!/usr/bin/env python3
"""In a text file, there is a single character H.
The text editor can execute only two operations in this file.Copy All and Paste
Given a number n, write a method that calculates
the fewest number of operations needed to result in exactly
n * H characters in the file.
"""


def minOperations(n: int) -> int:
    """Returns the minimum number of operations needed to achieve n H characters in the text file"""
    if n <= 1:
        return 0
    
    value = 0
    prime_num = 2
    
    while n > 1:
        while n % prime_num == 0:
            value += prime_num
            n //= prime_num
        prime_num += 1
    
    return value

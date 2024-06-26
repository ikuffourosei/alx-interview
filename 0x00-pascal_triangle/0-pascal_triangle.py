#!/usr/bin/python3
"""
This module defines a function that generates
Pascal's Triangle up to a given number of levels.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n levels.

    Args:
        n (int): The number of levels to generate in the triangle.

    Returns:
        list: A list of lists, where each
        inner list represents a level in Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

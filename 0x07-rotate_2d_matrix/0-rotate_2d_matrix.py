#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """A function that rotates a matrix by 90degrees"""
    if isinstance(matrix, list):
        row = len(matrix)
        for i in range(row):
            for j in range(i, row):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(row):
            matrix[i].reverse()
    else:
        return

#!/usr/bin/python3
"""Rotate 2D Matrix"""
# ways to solve
# convert given matrix to the transposed form
# return the reversed form of the transposed matrix


def rotate_2d_matrix(matrix):
    """A function that rotates a matrix by 90degrees"""
    # n x n matrix
    row = len(matrix)

    #find transpose
    for i in range(row):
        for j in range(i, row):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse matrix
    for i in range(row):
        matrix[i].reverse()

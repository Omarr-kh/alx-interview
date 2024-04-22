#!/usr/bin/python3
""" Algorithm for rotating a 2d matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """ rotate a 2d matrix 90 degrees clockwise """
    # Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

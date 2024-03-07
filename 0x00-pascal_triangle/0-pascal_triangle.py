#!/usr/bin/python3

"""
Generate Pascals triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascals triangle.
    """

    if n <= 0:
        return []

    pascal = []

    for i_row in range(n):
        row = []

        for j_col in range(i_row + 1):
            if j_col == 0 or j_col == i_row:
                row.append(1)
            else:
                column_val = pascal[i_row - 1][j_col] + pascal[i_row - 1][j_col - 1]
                row.append(column_val)
        pascal.append(row)
    return pascal

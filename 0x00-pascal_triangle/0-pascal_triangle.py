#!/usr/bin/python3

"""
Generate Pascals triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascals triangle.
    """

    # Check if n is less than or equal to 0
    if n <= 0:
        # If so, return an empty list
        return []

    # Initialize an empty list to store the Pascal's Triangle
    pascal = []

    # Iterate through each row up to the specified n
    for i_row in range(n):
        # Initialize an empty list for the current row
        row = []

        # Iterate through each column in the current row
        for j_col in range(i_row + 1):
            # Check if the current column is at the beginning or end of the row
            if j_col == 0 or j_col == i_row:
                # If so, set the value to 1 (edge values of Pascal's Triangle)
                row.append(1)
            else:
                # Calculate the value for the current non-edge column
                column_val = pascal[i_row - 1][j_col] + \
                    pascal[i_row - 1][j_col - 1]
                # Append the calculated value to the current row
                row.append(column_val)

        # Append the completed row to the Pascal's Triangle
        pascal.append(row)

    # Return the generated Pascal's Triangle
    return pascal

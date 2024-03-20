#!/usr/bin/python3
""" solution for minimum operations problem """


def minOperations(n):
    """ return min operations to get n 'H' """
    if n == 1:
        return 0  # No operations needed if there's only one H
    operations = float('inf')
    for i in range(2, n + 1):
        if n % i == 0:
            # If n is divisible by i, calculate the number of operations needed
            operations = min(operations, minOperations(n // i) + i)
    return operations

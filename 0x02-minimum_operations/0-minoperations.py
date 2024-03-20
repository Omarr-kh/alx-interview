#!/usr/bin/python3
""" solution for minimum operations problem """


def minOperations(n):
    """ return min operations to get n 'H' """
    if n == 1:
        return 0  # No operations needed if there's only one H

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = float('inf')
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                dp[i] = min(dp[i], dp[i // j] + j)
    return dp[n]

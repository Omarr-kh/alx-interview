#!/usr/bin/python3
""" solution for minimum operations problem """


def minOperations(n):
    """ return min operations to get n 'H' """
    if n == 1:
        return 0  # No operations needed if there's only one H

    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

        # For prime numbers, directly paste the content n-1 times after copying
        if dp[i] == float('inf'):
            dp[i] = i

    return dp[n]

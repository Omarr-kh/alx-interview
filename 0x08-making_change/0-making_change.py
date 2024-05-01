#!/usr/bin/python3
""" DP algorithm to solve Make Change """

def makeChange(coins, total):
    """ the algorithm to solve the make change problem """
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for a in range(1, total + 1):
        for c in coins:
            if (a - c) >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[total] if dp[total] != total + 1 else -1

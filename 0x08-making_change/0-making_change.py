#!/usr/bin/python3
""" DP algorithm to solve Make Change """


def makeChange(coins, total):
    """ the algorithm to solve the make change problem """
    if total <= 0:
        return -1

    coins = sorted(coins, reverse=True)
    i = 0
    coins_count = 0
    n = len(coins)
    while total > 0:
        if i >= n:
            return -1
        if total - coins[i] >= 0:
            total -= coins[i]
            coins_count += 1
        else:
            i += 1
    return coins_count

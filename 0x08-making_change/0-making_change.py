#!/usr/bin/python3
""" Solution to make change """


def makeChange(coins, total):
    """ greedy solution
    """
    if total <= 0:
        return 0
    rest = total
    total_coins = 0
    idx = 0
    coins_sorted = sorted(coins, reverse=True)
    n = len(coins)
    while rest > 0:
        if idx >= n:
            return -1
        if rest - coins_sorted[idx] >= 0:
            rest -= coins_sorted[idx]
            total_coins += 1
        else:
            idx += 1
    return total_coins

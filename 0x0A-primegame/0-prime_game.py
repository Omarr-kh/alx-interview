#!/usr/bin/python3
""" Solution for Prime Game Problem """


def isWinner(x, nums):
    """ Determine winner after x rounds """
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    max_n = max(nums)
    primes_list = [True for _ in range(max_n + 1)]
    primes_list[0] = False

    # Sieve of Eratosthenes to get primes
    for i, is_prime in enumerate(primes_list, 1):
        if i == 1 or is_prime == False:
            continue
        for k in range(i + i, max_n + 1, i):
            primes_list[k - 1] = False

    # loop through rounds and check n
    for _, m in zip(range(x), nums):
        round_n_primes = len(list(filter(lambda z: z, primes_list[0:m])))
        maria_wins += round_n_primes % 2 == 1
        ben_wins += round_n_primes % 2 == 0
    # can't determine winner
    if ben_wins == maria_wins:
        return None
    return 'Ben' if ben_wins > maria_wins else 'Maria'
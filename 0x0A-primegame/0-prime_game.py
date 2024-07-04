#!/usr/bin/python3
""" Check winner of a game """


def isWinner(x, nums):
    """ Check winner of a game """
    if x < 1 or not nums:
        return None

    maria_success = 0
    ben_success = 0

    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    for n in nums:
        count = sum(primes[2:n + 1])
        if count % 2 == 0:
            ben_success += 1
        else:
            maria_success += 1

    if maria_success == ben_success:
        return None

    return "Maria" if maria_success > ben_success else "Ben"

#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total
    """
    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0
    remaining = total

    for coin in coins:
        if coin <= remaining:
            # Maximum number of coins of this denomination
            num_coins = remaining // coin
            # Increase the count by the number of coins used
            coin_count += num_coins
            remaining -= coin * num_coins  # Decrease the remaining total

        if remaining == 0:
            break

    if remaining > 0:
        return -1  # It's not possible to meet the total with the given coins

    return coin_count

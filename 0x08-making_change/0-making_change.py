#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum coins for each amount
    # from 0 to total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # To make 0, we need 0 coins

    for coin in coins:
        for x in range(coin, total + 1):
            if min_coins[x - coin] != float('inf'):
                min_coins[x] = min(min_coins[x], min_coins[x - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1

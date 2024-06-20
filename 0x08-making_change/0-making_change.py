#!/usr/bin/python3
"""Implementing a gready Algorithm"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with infinity, and dp[0] = 0
    # because 0 coins are needed for 0 total
    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    # Loop through each coin and update the dp array
    for coin in coins:
        for x in range(coin, total + 1):
            if dp[x - coin] != float("inf"):
                dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[total] is still infinity, that means it's not possible
    # to form that total
    return dp[total] if dp[total] != float("inf") else -1

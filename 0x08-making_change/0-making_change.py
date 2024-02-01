#!/usr/bin/python3

"""
    Given a pile of coins of different values,
    the fewest number of coins needed to
    meet a given amount total are determined.
"""


def makeChange(coins, total):
    """ Function calculates num of coins"""
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins for each total
    # Initialize all values with a large number (greater than the given total)
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make a total of 0
    dp[0] = 0

    # Iterate through all possible totals from 1 to the given total
    for i in range(1, total + 1):
        # Iterate through all coin values
        for coin in coins:
            # Check if the coin value is less than or equal current total
            if coin <= i:
                # Update the minimum number of coins needed if using this coin
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If value in dp[total] remains unchanged, it means the total cannot be met
    if dp[total] == float('inf'):
        return -1

    return dp[total]
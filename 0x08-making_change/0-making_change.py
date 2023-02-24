#!/usr/bin/python3

"""
    Function to determine the fewest number of coins
    needed to give amount total

    args:
        coins - list of values coins in possession
        total -  the sum of the fewest coins
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # initialize the table with all values set to infinity
    # except for the first value, which is set to 0
    table = [float('inf')] * (total + 1)
    table[0] = 0

    # fill in the table for each amount up to the target amount
    for i in range(1, total + 1):
        # consider each coin value less than or equal to i
        for j in range(len(coins)):
            if coins[j] <= i:
                # add the minimum number of coins needed for the difference
                # between the current amount and the coin value
                table[i] = min(table[i], table[i - coins[j]] + 1)

    # return the minimum number of coins needed for the target amount
    return table[total] if table[total] != float('inf') else -1

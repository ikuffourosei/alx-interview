#!/usr/bin/python3
"""Making Change"""

def makeChange(coins, total):
    """Returns the fewest number of coins to meet total"""
    if total <= 0:
        return 0
    
    # Sort coins in descending order
    coins.sort(reverse=True)
    
    count = 0
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            num_coins = total // coin
            count += num_coins
            total -= num_coins * coin
    
    return count if total == 0 else -1

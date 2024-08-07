#!/usr/bin/python3
"""Prime factor game"""


def isWinner(x, nums):
    """A function that determines the winner of a prime factor game
    x: (int) - Number of rounds
    nums: [list] - nums is an array of n
    """
    if x <= 0 or not nums:
        return None

    max_num = max(nums)

    # Sieve of Eratosthenes
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(max_num ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_num + 1, start):
                sieve[multiple] = False

    prime_counts = [0] * (max_num + 1)
    count = 0
    for i in range(1, max_num + 1):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

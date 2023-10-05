#!/usr/bin/python3

""" This is a prime games that determines a winner when
    there are no longer any prime number to pick from.
"""


def isWinner(x, nums):
    """Function that determines the winner."""
    wins = {"Maria": 0, "Ben": 0}

    def is_prime(num):
        """Helper function to check if a number is prime"""

        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(x):
        n = nums[i]
        primes = [num for num in range(2, n + 1) if is_prime(num)]
        game_over = False
        turn = "Maria"

        while not game_over:
            # Maria's turn
            if turn == "Maria":
                if not primes:
                    wins["Ben"] += 1
                    game_over = True
                else:
                    num = primes.pop(0)
                    primes = [p for p in primes if p % num != 0]
                    turn = "Ben"
            # Ben's turn
            else:
                if not primes:
                    wins["Maria"] += 1
                    game_over = True
                else:
                    num = primes.pop(0)
                    primes = [p for p in primes if p % num != 0]
                    turn = "Maria"

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None

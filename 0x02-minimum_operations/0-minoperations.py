#!/usr/bin/python3

""" This is a method that contains
an algorithm that calculates the fewest number of operations
needed to result n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0

Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH =>
Copy All => Paste => HHHHHH =>
Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    """This is the function that calculates
     the number of operations."""

    if n <= 1:
        return 0

    num, div, numOfOperations = n, 2, 0

    while num > 1:
        if num % div == 0:
            num = num / div
            numOfOperations = numOfOperations + div
        else:
            div += 1

    return numOfOperations

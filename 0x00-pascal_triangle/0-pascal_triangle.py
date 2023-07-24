#!/usr/bin/python3

"""A function that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """function that creates pascal's triangle"""

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prevRow = triangle[-1]
        nextRow = [1]

        for j in range(1, i):
            nextRow.append(prevRow[j - 1] + prevRow[j])

        nextRow.append(1)
        triangle.append(nextRow)

    return triangle

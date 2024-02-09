#!/usr/bin/python3

"""
function def island_perimeter(grid): that returns the perimeter
of the island described in grid
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    if not grid or not grid[0]:
        return 0

    rows = len(grid)  # this would give us the row length
    cols = len(grid[0])  # this would give us how many columns
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Assume that all sides part of perimeter

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
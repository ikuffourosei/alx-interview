#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    A function that calculates the perimeter of an island
    in a grid

    Parameter: grid
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check the four possible sides
                # Check up
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                # Check down
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1
                # Check left
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                # Check right
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter

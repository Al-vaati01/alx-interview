#!/usr/bin/python3
"""calculate perimeter"""


def island_perimeter(grid):
    """grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        returns the perimeter of the island described in grid
    """
    perimeter = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            idx = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            check = [1 if k[0] in range(row) and k[1] in range(col) else 0
                     for k in idx]

            if grid[i][j]:
                perimeter += sum([1 if not r or not grid[k[0]][k[1]] else 0
                                  for r, k in zip(check, idx)])
    return perimeter

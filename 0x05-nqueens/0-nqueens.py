#!/usr/bin/python3
"""N Queens problem
input 6

output

[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
"""


def nqueens(n):
    """
    Solves the N queens problem.

    Args:
      n: The number of queens.

    Returns:
      A list of lists, where each inner list represents a row of queens.
    """
    solutions = []
    for i in range(n):
        solution = [[False for j in range(n)] for k in range(n)]
        solution[i][0] = True
        if _solve(solution, 1):
            solutions.append(solution)
    return solutions


def _solve(solution, row):
    """
    Recursively solves the N queens problem for a given row.

    Args:
      solution: The current solution.
      row: The current row.

    Returns:
      True if the solution is valid, False otherwise.
    """
    if row == len(solution[0]):
        return True
    for col in range(len(solution[0])):
        if _is_valid(solution, row, col):
            solution[row][col] = True
            if _solve(solution, row + 1):
                return True
            solution[row][col] = False
    return False


def _is_valid(solution, row, col):
    """
    Checks if a queen can be placed at the given row and column.

    Args:
      solution: The current solution.
      row: The current row.
      col: The current column.

    Returns:
      True if the queen can be placed, False otherwise.
    """
    for i in range(row):
        if solution[i][col]:
            return False
    for i in range(row):
        for j in range(col):
            if solution[i][j] and (col - j == row - i or col + j == row - i):
                return False
    return True

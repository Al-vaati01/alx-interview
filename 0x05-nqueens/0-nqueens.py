#!/usr/bin/python3
"""N Queens problem
input 6

output

[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
"""
import sys


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
            solutions.append(_get_solution_list(solution))
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


def _get_solution_list(solution):
    """
    Converts the solution from a 2D array to a list of lists.

    Args:
      solution: The solution as a 2D array.

    Returns:
      A list of lists, where each inner list represents a row of queens.
    """
    solution_list = []
    for i in range(len(solution)):
        solution_list.append([solution[i][j] for j in range(len(solution[0]))])
    return solution_list


input = sys.argv
if len(input) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(input[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
solutions = nqueens(n)
for solution in solutions:
    print(solution)

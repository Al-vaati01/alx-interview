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
      A list of solutions, where each solution is a list of queen positions.
    """
    solutions = []
    for i in range(n):
        solution = [-1] * n
        solution[0] = i
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
    if row == len(solution):
        return True
    for col in range(len(solution)):
        if _is_valid(solution, row, col):
            solution[row] = col
            if _solve(solution, row + 1):
                return True
            solution[row] = -1
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
        if solution[i] == col or abs(solution[i] - col) == abs(i - row):
            return False
    return True


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

solutions = nqueens(n)
for solution in solutions:
    solution_list = [[row, col] for row, col in enumerate(solution)]
    for row, col in solution_list:
        print(f"[{row}, {col}]", end=" ")
    print()

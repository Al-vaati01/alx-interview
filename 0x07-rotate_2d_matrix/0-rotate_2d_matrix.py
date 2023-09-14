#!/usr/bin/python3
"""Matrix Rotation

This script defines a function to rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix) -> None:
    """Rotates 2d matrix"""
    def are_all_equal(lst):
        """Check if all elements in the list are equal."""
        # Check if the list is empty
        if not lst:
            return False
        # Compare all elements to the first element
        first_element = lst[0]
        return all(element == first_element for element in lst)

    # Check if the input is a valid matrix
    row_lengths = [len(row) for row in matrix]
    if not are_all_equal(row_lengths):
        print("Not a valid matrix")
        return

    n = len(matrix)

    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the 90-degree clockwise rotation
    for i in range(n):
        matrix[i].reverse()

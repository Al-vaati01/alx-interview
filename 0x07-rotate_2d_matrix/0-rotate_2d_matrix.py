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

    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = []

    # Rotate the matrix 90 degrees clockwise
    for i in range(cols):
        temp = []
        for j in range(rows):
            temp.append(matrix[rows - j - 1][i])
        new_matrix.append(temp)

    # Print the rotated matrix
    for row in new_matrix:
        print(row)

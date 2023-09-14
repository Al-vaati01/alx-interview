# Rotate 2D Matrix Task

This README provides an overview of the "Rotate 2D Matrix" script, including its description, prototype, and an example usage of the provided Python script.

### Objective

Given an n x n 2D matrix, the goal of this task is to rotate it 90 degrees clockwise in-place.

### Prototype

The function to implement is as follows:

```
def rotate_2d_matrix(matrix):
```

**Note:**
- The function should not return anything.
- The rotation operation should be performed directly on the input matrix.
- You can assume that the matrix will have two dimensions and will not be empty.

### Example Usage

To demonstrate how to use the rotate_2d_matrix function, we've provided a sample Python script main_0.py:

```
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```

### Running the Script

You can execute the script as follows:

```
./main_0.py
```
### Expected Output

After running the script, you should see the following output:

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

This output demonstrates the result of rotating the input matrix matrix 90 degrees clockwise.

Feel free to modify the input matrix in the script to test with other 2D matrices.
#!/usr/bin/python3
"""Pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    rows of the Pascal’s triangle of n number of rows"""
    list = []
    if n <= 0:
        return []
    for i in range(n):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(list[i - 1][j - 1] + list[i - 1][j])
        list.append(temp_list)
    return list

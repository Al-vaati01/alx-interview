#!/usr/bin/env python3
"""
a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    def search(box_index, visited):
        visited[box_index] = True
        for key in boxes[box_index]:
            if not visited[key]:
                search(key, visited)

    num_boxes = len(boxes)
    visited = [False] * num_boxes

    search(0, visited)

    return all(visited)

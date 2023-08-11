#!/usr/bin/python3

"""Contains a function that takes on a list of list (boxes)
    and determines if they can all be unlocked or not."""


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened."""
    total_boxes = len(boxes)
    visited = set()
    stack = [0]  # Start from box 0 (the first box)

    while stack:
        box = stack.pop()  # this initially gives box the value 0 :)
        visited.add(box)

        # Check all the keys in the current box
        for key in boxes[box]:
            # If the key opens a new box that hasn't been visited yet,
            # add it to the stack
            if key not in visited and key >= 0 and key < total_boxes:
                stack.append(key)

    # If all boxes have been visited, then all boxes can be opened
    return len(visited) == total_boxes

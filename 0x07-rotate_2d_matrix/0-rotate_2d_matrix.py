#!/usr/bin/python3

""" This module rotates a 2D matrix clockwise."""


def rotate_2d_matrix(matrix):
    # transpose matrix (push box (matrix) over from left to right)
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse matrix (first row becomes last, last row becomes first)
    lengthOfArray = len(matrix)
    for i in range(lengthOfArray // 2):
        for j in range(lengthOfArray):
            matrix[j][i], matrix[j][lengthOfArray - 1 - i] = (
                matrix[j][lengthOfArray - 1 - i], matrix[j][i]
            )


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

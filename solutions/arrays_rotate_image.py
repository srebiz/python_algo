from typing import List


def rotate_image(matrix: List[List[int]]) -> List[List[int]]:
    """
    Rotate an n x n matrix 90 degrees clockwise, in place.

    Transpose (swap across the main diagonal), then reverse each row.

    Time:  O(n^2).  Space: O(1).
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

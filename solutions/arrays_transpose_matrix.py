from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    """
    Return the transpose (rows become columns). Works for non-square matrices,
    so a new matrix is allocated rather than swapping in place.

    Time:  O(m * n).  Space: O(m * n).
    """
    if not matrix or not matrix[0]:
        return []
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]

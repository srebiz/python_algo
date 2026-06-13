from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Return matrix elements in clockwise spiral order. Covers "Spiral Matrix"
    and "Traversal of Spiral Matrix".

    Maintain four shrinking boundaries (top/bottom/left/right); peel one edge
    per step.

    Time:  O(m * n).  Space: O(1) beyond the output.
    """
    if not matrix or not matrix[0]:
        return []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    out: List[int] = []
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            out.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):
            out.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                out.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                out.append(matrix[r][left])
            left += 1
    return out

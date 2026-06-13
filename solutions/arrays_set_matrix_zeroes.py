from typing import List


def set_matrix_zeroes(matrix: List[List[int]]) -> List[List[int]]:
    """
    If a cell is 0, set its entire row and column to 0, in place.

    Use the first row/column as marker storage (O(1) extra space); two flags
    remember whether the first row/column themselves must be zeroed.

    Time:  O(m * n).  Space: O(1).
    """
    if not matrix or not matrix[0]:
        return matrix
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
    first_col_zero = any(matrix[r][0] == 0 for r in range(rows))
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = matrix[0][c] = 0
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    if first_row_zero:
        for c in range(cols):
            matrix[0][c] = 0
    if first_col_zero:
        for r in range(rows):
            matrix[r][0] = 0
    return matrix

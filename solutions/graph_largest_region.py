from typing import List


def largest_region(matrix: List[List[int]]) -> int:
    """
    Size of the largest connected region of 1s in a boolean matrix, counting all
    8 directions (including diagonals).

    DFS from each unvisited 1, summing the region size; mark visited in place.

    Time:  O(m * n).  Space: O(m * n) recursion worst case.
    """
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])

    def dfs(r: int, c: int) -> int:
        if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] != 1:
            return 0
        matrix[r][c] = -1                 # mark visited
        size = 1
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr or dc:
                    size += dfs(r + dr, c + dc)
        return size

    best = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                best = max(best, dfs(r, c))
    return best

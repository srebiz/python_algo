from typing import List


def unique_paths_with_obstacles(grid: List[List[int]]) -> int:
    """
    Count paths from top-left to bottom-right moving only right/down, where
    grid cells equal to 1 are obstacles.

    1-D DP across columns; an obstacle zeroes its cell's path count.

    Time:  O(m * n).  Space: O(n).
    """
    if not grid or grid[0][0] == 1:
        return 0
    cols = len(grid[0])
    dp = [0] * cols
    dp[0] = 1
    for row in grid:
        for c in range(cols):
            if row[c] == 1:
                dp[c] = 0
            elif c > 0:
                dp[c] += dp[c - 1]
    return dp[-1]

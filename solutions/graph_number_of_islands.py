from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """
    Count connected groups of '1' (land) cells; neighbours are up/down/left/right.

    DFS that sinks each visited land cell to '0' so it isn't recounted.

    Time:  O(m * n).  Space: O(m * n) recursion worst case.
    """
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])

    def sink(r: int, c: int) -> None:
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
            grid[r][c] = "0"
            sink(r + 1, c); sink(r - 1, c); sink(r, c + 1); sink(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                sink(r, c)
    return count

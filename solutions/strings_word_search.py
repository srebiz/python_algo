from typing import List


def word_search(board: List[List[str]], word: str) -> bool:
    """
    Return True if `word` can be traced in the grid via adjacent (up/down/
    left/right) cells without reusing a cell. (Also covers "Existence of a Word".)

    DFS backtracking from each cell; mark visited in place with a sentinel and
    restore on the way out.

    Time:  O(m * n * 4^L) — L = len(word).  Space: O(L) recursion depth.
    """
    if not board or not board[0]:
        return False
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, i: int) -> bool:
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False
        saved, board[r][c] = board[r][c], "#"
        found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                 dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
        board[r][c] = saved
        return found

    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))

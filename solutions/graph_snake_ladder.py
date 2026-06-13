from collections import deque
from typing import Dict


def snakes_and_ladders(board_size: int, jumps: Dict[int, int]) -> int:
    """
    Fewest dice rolls to go from square 1 to `board_size`. `jumps` maps a square
    to its snake/ladder destination.

    BFS over squares (each is a graph node); from a square you can reach the next
    six, then follow any jump. Returns -1 if unreachable.

    Time:  O(board_size).  Space: O(board_size).
    """
    visited = [False] * (board_size + 1)
    queue = deque([(1, 0)])               # (square, rolls)
    visited[1] = True
    while queue:
        square, rolls = queue.popleft()
        if square == board_size:
            return rolls
        for die in range(1, 7):
            nxt = square + die
            if nxt > board_size:
                break
            nxt = jumps.get(nxt, nxt)     # take the ladder/snake if present
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, rolls + 1))
    return -1

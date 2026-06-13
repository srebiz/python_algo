from __future__ import annotations
from collections import deque
from typing import List, Optional
from .trees_common import TreeNode


def right_view(root: Optional[TreeNode]) -> List[int]:
    """
    Values visible from the right side, top to bottom (the last node of each level).

    Level-order BFS; the last node dequeued per level is the visible one.

    Time:  O(n).  Space: O(w) — w = max level width.
    """
    if not root:
        return []
    out: List[int] = []
    queue = deque([root])
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if i == size - 1:
                out.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return out

from __future__ import annotations
from collections import deque
from typing import List, Optional
from .trees_common import TreeNode


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Breadth-first traversal grouped by level.

    BFS, snapshotting each level's width before draining it.

    Time:  O(n).  Space: O(w).
    """
    if not root:
        return []
    out: List[List[int]] = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        out.append(level)
    return out

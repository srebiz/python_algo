from __future__ import annotations
from typing import Optional
from .trees_common import TreeNode


def height(root: Optional[TreeNode]) -> int:
    """
    Height = number of nodes on the longest root-to-leaf path. Empty tree -> 0.

    Post-order recursion: a node's height is 1 + the taller of its subtrees.

    Time:  O(n).  Space: O(h) recursion stack.
    """
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

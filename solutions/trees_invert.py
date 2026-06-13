from __future__ import annotations
from typing import Optional
from .trees_common import TreeNode


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Mirror a binary tree: swap every node's left and right children.

    Time:  O(n).  Space: O(h).
    """
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

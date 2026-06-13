from __future__ import annotations
from typing import Optional
from .trees_common import TreeNode


def is_subtree(root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
    """
    Return True if `sub` is a subtree of `root` (same structure and values
    rooted at some node).

    For each node of root, test exact-match against sub.

    Time:  O(m * n) worst case.  Space: O(h).
    """
    def same(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if a is None and b is None:
            return True
        if a is None or b is None or a.val != b.val:
            return False
        return same(a.left, b.left) and same(a.right, b.right)

    if sub is None:
        return True
    if root is None:
        return False
    return same(root, sub) or is_subtree(root.left, sub) or is_subtree(root.right, sub)

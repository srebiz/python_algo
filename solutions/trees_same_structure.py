from __future__ import annotations
from typing import Optional
from .trees_common import TreeNode


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Return True if two trees are structurally identical with equal values.
    ("Check if Two Trees Have Same Structure.")

    Recurse in lockstep; both must be None together or match value-and-shape.

    Time:  O(n).  Space: O(h).
    """
    if p is None and q is None:
        return True
    if p is None or q is None or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

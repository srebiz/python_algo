from __future__ import annotations
from typing import Optional
from .trees_common import TreeNode


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Validate a Binary Search Tree. Covers "Validation of a Binary Tree" and
    "Validate Binary Search Tree".

    Each node must fall inside an open (low, high) interval; recurse tightening
    the bound. Checking only direct children misses deep violations.

    Time:  O(n).  Space: O(h).
    """
    def valid(node: Optional[TreeNode], low: float, high: float) -> bool:
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)

    return valid(root, float("-inf"), float("inf"))

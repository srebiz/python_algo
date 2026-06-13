from __future__ import annotations
from typing import Optional
from .trees_common import TreeNode


def kth_smallest(root: Optional[TreeNode], k: int) -> Optional[int]:
    """
    The k-th smallest value (1-indexed) in a BST, or None if k is out of range.

    Iterative inorder traversal yields values in ascending order; stop at the
    k-th popped node without traversing the whole tree.

    Time:  O(h + k).  Space: O(h).
    """
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
    return None

from __future__ import annotations
from typing import List, Optional
from .trees_common import TreeNode


def build_from_preorder_inorder(preorder: List[int],
                                inorder: List[int]) -> Optional[TreeNode]:
    """
    Reconstruct a binary tree from its preorder and inorder traversals
    (assuming unique values).

    Preorder's first element is the root; its index in inorder splits left/right
    subtrees. An index map + a moving preorder pointer keeps it O(n).

    Time:  O(n).  Space: O(n).
    """
    index = {val: i for i, val in enumerate(inorder)}
    pre_pos = 0

    def build(lo: int, hi: int) -> Optional[TreeNode]:
        nonlocal pre_pos
        if lo > hi:
            return None
        root_val = preorder[pre_pos]
        pre_pos += 1
        node = TreeNode(root_val)
        mid = index[root_val]
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(inorder) - 1)

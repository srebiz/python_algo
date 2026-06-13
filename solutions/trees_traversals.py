from __future__ import annotations
from typing import List, Optional
from .trees_common import TreeNode


def inorder(root: Optional[TreeNode]) -> List[int]:
    """Left, node, right. For a BST this yields sorted order. O(n) time, O(h) space."""
    out: List[int] = []

    def go(node: Optional[TreeNode]) -> None:
        if node:
            go(node.left); out.append(node.val); go(node.right)

    go(root)
    return out


def preorder(root: Optional[TreeNode]) -> List[int]:
    """Node, left, right. O(n) time, O(h) space."""
    out: List[int] = []

    def go(node: Optional[TreeNode]) -> None:
        if node:
            out.append(node.val); go(node.left); go(node.right)

    go(root)
    return out


def postorder(root: Optional[TreeNode]) -> List[int]:
    """Left, right, node. O(n) time, O(h) space."""
    out: List[int] = []

    def go(node: Optional[TreeNode]) -> None:
        if node:
            go(node.left); go(node.right); out.append(node.val)

    go(root)
    return out

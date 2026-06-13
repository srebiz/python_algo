from __future__ import annotations
from typing import List


class NaryNode:
    """An N-ary tree node with an ordered list of children."""

    def __init__(self, val: int, children: "List[NaryNode] | None" = None) -> None:
        self.val = val
        self.children: List[NaryNode] = children or []


def is_mirror_of_itself(root: NaryNode | None) -> bool:
    """
    Return True if an N-ary tree is a mirror image of itself (symmetric).

    Compare two cursors moving inward: children read left-to-right on one side
    must equal right-to-left on the other, recursively (values + structure).

    Time:  O(n).  Space: O(h * branching) recursion.
    """
    def mirror(a: NaryNode | None, b: NaryNode | None) -> bool:
        if a is None and b is None:
            return True
        if a is None or b is None or a.val != b.val:
            return False
        if len(a.children) != len(b.children):
            return False
        return all(mirror(a.children[i], b.children[len(b.children) - 1 - i])
                   for i in range(len(a.children)))

    if root is None:
        return True
    return mirror(root, root)

"""Shared singly-linked-list node and helpers used across the linked-list
exercises. Importing one definition keeps node identity consistent across files.
"""
from __future__ import annotations
from typing import List, Optional


class ListNode:
    """A singly-linked-list node."""

    def __init__(self, val: int = 0, nxt: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = nxt

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def build_list(values: List[int]) -> Optional[ListNode]:
    """Build a linked list from a Python list; return its head. O(n)."""
    head: Optional[ListNode] = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_pylist(head: Optional[ListNode], limit: int = 100) -> List[int]:
    """Convert a linked list back to a Python list. `limit` guards cycles. O(n)."""
    out: List[int] = []
    node = head
    while node and len(out) < limit:
        out.append(node.val)
        node = node.next
    return out

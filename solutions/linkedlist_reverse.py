from __future__ import annotations
from typing import Optional
from .linkedlist_common import ListNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list and return the new head.

    Iteratively flip each node's `next` pointer while walking forward.

    Time:  O(n).  Space: O(1).
    """
    prev: Optional[ListNode] = None
    cur = head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev

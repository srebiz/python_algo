from __future__ import annotations
from typing import Optional
from .linkedlist_common import ListNode


def remove_duplicates_sorted(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Remove duplicate values from a *sorted* linked list, keeping one of each.

    Single pass: skip a node whose value equals the current node's.

    Time:  O(n).  Space: O(1).
    """
    cur = head
    while cur and cur.next:
        if cur.next.val == cur.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

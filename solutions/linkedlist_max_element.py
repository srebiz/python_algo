from __future__ import annotations
from typing import Optional
from .linkedlist_common import ListNode


def max_element(head: Optional[ListNode]) -> Optional[int]:
    """
    Return the largest value in the list, or None if empty.

    Time:  O(n).  Space: O(1).
    """
    if not head:
        return None
    best = head.val
    cur = head.next
    while cur:
        if cur.val > best:
            best = cur.val
        cur = cur.next
    return best

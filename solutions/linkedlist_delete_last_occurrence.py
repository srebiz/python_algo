from __future__ import annotations
from typing import Optional
from .linkedlist_common import ListNode


def delete_last_occurrence(head: Optional[ListNode], target: int) -> Optional[ListNode]:
    """
    Delete the last node equal to target. One pass remembers the predecessor of
    the most recent match; a second-free unlink follows.

    Time:  O(n).  Space: O(1).
    """
    dummy = ListNode(0, head)
    last_prev: Optional[ListNode] = None
    prev = dummy
    while prev.next:
        if prev.next.val == target:
            last_prev = prev
        prev = prev.next
    if last_prev:
        last_prev.next = last_prev.next.next
    return dummy.next

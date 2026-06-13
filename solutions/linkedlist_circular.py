from __future__ import annotations
from typing import Optional
from .linkedlist_common import ListNode


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect whether a linked list contains a cycle (Floyd's tortoise & hare).
    A fast pointer moving two steps meets a slow one-step pointer iff a loop exists.

    Time:  O(n).  Space: O(1).
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

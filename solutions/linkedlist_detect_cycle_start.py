from __future__ import annotations
from typing import Optional
from .linkedlist_common import ListNode


def detect_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Return the node where a cycle begins, or None. ("Node of Circular Linked List.")

    Floyd's algorithm: after slow/fast meet, advancing one pointer from the head
    and one from the meeting point at equal speed makes them meet at the entry.

    Time:  O(n).  Space: O(1).
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            ptr = head
            while ptr is not slow:
                ptr = ptr.next
                slow = slow.next
            return ptr
    return None

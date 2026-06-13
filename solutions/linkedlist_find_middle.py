from __future__ import annotations
from typing import Optional
from .linkedlist_common import ListNode


def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Return the middle node (the second middle for even length).

    Slow/fast pointers: when fast reaches the end, slow sits at the middle.

    Time:  O(n).  Space: O(1).
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

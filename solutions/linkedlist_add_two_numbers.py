from __future__ import annotations
from typing import Optional
from builders import linkedlist_common


def add_two_numbers(l1: Optional[linkedlist_common.ListNode], l2: Optional[linkedlist_common.ListNode]) -> Optional[linkedlist_common.ListNode]:
    """
    Two numbers are stored as linked lists with digits in reverse order; return
    their sum in the same form. (342) + (465) -> 7 -> 0 -> 8 i.e. 807.

    Walk both lists adding digit + carry, building the result as we go.

    Time:  O(max(m, n)).  Space: O(max(m, n)).
    """
    dummy = tail = linkedlist_common.ListNode()
    carry = 0
    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val; l1 = l1.next
        if l2:
            total += l2.val; l2 = l2.next
        carry, digit = divmod(total, 10)
        tail.next = ListNode(digit)
        tail = tail.next
    return dummy.next

from __future__ import annotations
from typing import List, Optional
from .linkedlist_common import ListNode


class SinglyLinkedList:
    """
    A basic singly linked list supporting append, prepend, delete, and search.

    append:  O(n) (tracks a tail pointer would make it O(1); kept simple here).
    prepend: O(1).
    delete:  O(n).  search: O(n).  Space: O(n).
    """

    def __init__(self) -> None:
        self.head: Optional[ListNode] = None

    def prepend(self, val: int) -> None:
        self.head = ListNode(val, self.head)

    def append(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def delete(self, val: int) -> bool:
        dummy = ListNode(0, self.head)
        prev = dummy
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
                self.head = dummy.next
                return True
            prev = prev.next
        return False

    def search(self, val: int) -> bool:
        cur = self.head
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False

    def to_list(self) -> List[int]:
        out, cur = [], self.head
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out

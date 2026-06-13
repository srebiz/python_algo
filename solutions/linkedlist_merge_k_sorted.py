from __future__ import annotations
import heapq
from typing import List, Optional
from .linkedlist_common import ListNode


def merge_k_sorted(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists into one sorted list.

    Min-heap of the current head of each list; pop the smallest, push its next.
    A counter tie-breaker avoids comparing ListNode objects when vals are equal.

    Time:  O(N log k) — N = total nodes.  Space: O(k).
    """
    heap: list = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = tail = ListNode()
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next

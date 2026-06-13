import heapq
from typing import List, Optional


def largest_triplet_products(stream: List[int]) -> List[Optional[int]]:
    """
    For each incoming number, report the product of the three largest values
    seen so far, or None until at least three exist.

    Keep a min-heap of size 3 holding the current top-3; its product is the answer.

    Time:  O(n log 3) = O(n).  Space: O(1).
    """
    top3: list[int] = []
    out: List[Optional[int]] = []
    for x in stream:
        heapq.heappush(top3, x)
        if len(top3) > 3:
            heapq.heappop(top3)
        out.append(top3[0] * top3[1] * top3[2] if len(top3) == 3 else None)
    return out

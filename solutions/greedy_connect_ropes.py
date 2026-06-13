import heapq
from typing import List


def min_cost_connect_ropes(lengths: List[int]) -> int:
    """
    Connect all ropes into one; the cost to join two ropes is their combined
    length. Minimize total cost.

    Greedy with a min-heap: always join the two shortest ropes first, so short
    ropes (which get re-added to later joins) are charged fewest times.

    Time:  O(n log n).  Space: O(n).
    """
    if len(lengths) < 2:
        return 0
    heap = lengths[:]
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        total += a + b
        heapq.heappush(heap, a + b)
    return total

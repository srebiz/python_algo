import heapq


class MedianFinder:
    """
    Maintain a running median as numbers stream in.

    Two heaps: a max-heap (`lo`, negated) for the smaller half and a min-heap
    (`hi`) for the larger half, kept balanced in size. The median is the top of
    the larger heap, or the average of both tops.

    add_num:     O(log n).
    find_median: O(1).
    Space:       O(n).
    """

    def __init__(self) -> None:
        self._lo: list[int] = []   # max-heap via negation
        self._hi: list[int] = []   # min-heap

    def add_num(self, num: int) -> None:
        heapq.heappush(self._lo, -num)
        heapq.heappush(self._hi, -heapq.heappop(self._lo))
        if len(self._hi) > len(self._lo):
            heapq.heappush(self._lo, -heapq.heappop(self._hi))

    def find_median(self) -> float:
        if len(self._lo) > len(self._hi):
            return float(-self._lo[0])
        return (-self._lo[0] + self._hi[0]) / 2.0

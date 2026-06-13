from typing import List


def min_chocolate_diff(packets: List[int], students: int) -> int:
    """
    Distribute one packet per student so the gap between the largest and
    smallest given packet is minimized; return that minimum gap.

    Sort, then slide a window of size `students`; the best window has the
    smallest end-to-end span.

    Time:  O(n log n).  Space: O(1).
    """
    if students == 0 or len(packets) < students:
        return 0
    packets.sort()
    best = float("inf")
    for i in range(len(packets) - students + 1):
        best = min(best, packets[i + students - 1] - packets[i])
    return int(best)

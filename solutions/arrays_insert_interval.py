from typing import List


def insert_interval(intervals: List[List[int]], new: List[int]) -> List[List[int]]:
    """
    Insert a new interval into a list of sorted, non-overlapping intervals and
    merge any overlaps.

    Three phases: copy intervals ending before `new`, merge all that overlap
    `new`, then copy the rest.

    Time:  O(n).  Space: O(n).
    """
    out: List[List[int]] = []
    i, n = 0, len(intervals)
    while i < n and intervals[i][1] < new[0]:
        out.append(intervals[i]); i += 1
    while i < n and intervals[i][0] <= new[1]:
        new = [min(new[0], intervals[i][0]), max(new[1], intervals[i][1])]
        i += 1
    out.append(new)
    while i < n:
        out.append(intervals[i]); i += 1
    return out

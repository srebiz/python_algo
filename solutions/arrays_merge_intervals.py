from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge all overlapping intervals.

    Sort by start; for each interval, extend the last kept interval if they
    overlap, otherwise append a new one.

    Time:  O(n log n).  Space: O(n).
    """
    if not intervals:
        return []
    intervals.sort(key=lambda iv: iv[0])
    merged = [intervals[0][:]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

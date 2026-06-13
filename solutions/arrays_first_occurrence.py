from typing import List


def first_occurrence(nums: List[int], target: int) -> int:
    """
    Index of the first occurrence of target, or -1. (Linear; for sorted input
    see arrays_first_last_position for the O(log n) variant.)

    Time:  O(n).  Space: O(1).
    """
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1

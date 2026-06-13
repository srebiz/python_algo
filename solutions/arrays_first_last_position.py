from typing import List, Tuple
import bisect


def first_last_position(nums: List[int], target: int) -> Tuple[int, int]:
    """
    First and last index of target in a sorted list, or (-1, -1) if absent.

    Two binary searches via bisect_left / bisect_right.

    Time:  O(log n).  Space: O(1).
    """
    left = bisect.bisect_left(nums, target)
    if left == len(nums) or nums[left] != target:
        return -1, -1
    right = bisect.bisect_right(nums, target) - 1
    return left, right

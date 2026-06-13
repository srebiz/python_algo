from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """
    Index of target in a sorted list, or -1. Iterative, overflow-safe midpoint.

    Time:  O(log n).  Space: O(1).
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

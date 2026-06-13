from typing import List


def search_rotated(nums: List[int], target: int) -> int:
    """
    Search a rotated sorted array (no duplicates); return index or -1.

    Modified binary search: one half of [lo, hi] is always sorted; check
    whether target lies in that sorted half to decide which way to go.

    Time:  O(log n).  Space: O(1).
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:                 # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                     # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

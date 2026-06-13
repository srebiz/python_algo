from typing import List


def linear_search(nums: List[int], target: int) -> int:
    """
    Return the index of the first occurrence of target, or -1.

    Time:  O(n).  Space: O(1).
    """
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1

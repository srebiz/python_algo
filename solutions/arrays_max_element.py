from typing import List, Optional


def max_element(nums: List[int]) -> Optional[int]:
    """
    Return the maximum element, or None for an empty list.

    Single linear scan tracking the running maximum.

    Time:  O(n).  Space: O(1).
    """
    if not nums:
        return None
    best = nums[0]
    for x in nums[1:]:
        if x > best:
            best = x
    return best

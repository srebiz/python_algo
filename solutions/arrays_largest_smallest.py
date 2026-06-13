from typing import List, Optional, Tuple


def largest_and_smallest(nums: List[int]) -> Optional[Tuple[int, int]]:
    """
    Return (largest, smallest) in a single pass, or None if empty.

    Time:  O(n).  Space: O(1).
    """
    if not nums:
        return None
    largest = smallest = nums[0]
    for x in nums[1:]:
        if x > largest:
            largest = x
        elif x < smallest:
            smallest = x
    return largest, smallest

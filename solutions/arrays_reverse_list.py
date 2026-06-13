from typing import List


def reverse_list(nums: List[int]) -> List[int]:
    """
    Reverse the list in place and return it (two-pointer swap).

    Time:  O(n).  Space: O(1).
    """
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

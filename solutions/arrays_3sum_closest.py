from typing import List


def three_sum_closest(nums: List[int], target: int) -> int:
    """
    Sum of the triplet whose total is closest to target.

    Sort, fix one index, two-pointer the rest; track the closest sum seen.

    Time:  O(n^2).  Space: O(1).
    """
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if abs(total - target) < abs(closest - target):
                closest = total
            if total < target:
                lo += 1
            elif total > target:
                hi -= 1
            else:
                return total
    return closest

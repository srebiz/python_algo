from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    All unique triplets that sum to zero.

    Sort, fix index i, then two-pointer the remainder. Skip duplicate values at
    every level to keep triplets unique.

    Time:  O(n^2).  Space: O(1) beyond the output.
    """
    nums.sort()
    out: List[List[int]] = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break
        lo, hi = i + 1, n - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total < 0:
                lo += 1
            elif total > 0:
                hi -= 1
            else:
                out.append([nums[i], nums[lo], nums[hi]])
                lo += 1; hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
    return out

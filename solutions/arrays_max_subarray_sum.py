from typing import List


def max_subarray_sum(nums: List[int]) -> int:
    """
    Maximum sum of any contiguous non-empty subarray (Kadane's algorithm).
    Covers both "Largest Subarray Sum" and "Max Subarray Sum".

    Carry the best sum ending at i; extend the previous run or restart at nums[i],
    whichever is larger.

    Time:  O(n).  Space: O(1).
    """
    best = current = nums[0]
    for x in nums[1:]:
        current = max(x, current + x)
        best = max(best, current)
    return best

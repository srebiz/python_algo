from typing import List


def count_triplets_below_sum(nums: List[int], target: int) -> int:
    """
    Count triplets (i < j < k) whose sum is strictly less than `target`.

    Sort, then for each fixed left index use two pointers: when nums[i] +
    nums[lo] + nums[hi] < target, every element between lo and hi also works
    with lo, so (hi - lo) triplets are added at once; advance lo. Otherwise
    shrink hi. This collapses an O(n^3) brute force to O(n^2).

    Time:  O(n^2).  Space: O(1) (in-place sort).
    """
    nums.sort()
    n = len(nums)
    count = 0
    for i in range(n - 2):
        lo, hi = i + 1, n - 1
        while lo < hi:
            if nums[i] + nums[lo] + nums[hi] < target:
                count += hi - lo        # all (lo..hi-1) pair with hi fixed-left
                lo += 1
            else:
                hi -= 1
    return count

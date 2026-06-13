import bisect
from typing import List


def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    Length of the longest strictly increasing subsequence.

    Patience sorting: `tails[i]` is the smallest possible tail of an increasing
    subsequence of length i+1. Binary-search each value into `tails`.

    Time:  O(n log n).  Space: O(n).
    """
    tails: List[int] = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

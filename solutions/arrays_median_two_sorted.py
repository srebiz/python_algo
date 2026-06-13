from typing import List


def median_two_sorted(a: List[int], b: List[int]) -> float:
    """
    Median of two sorted arrays in O(log(min(m, n))).

    Binary search a partition of the smaller array so that everything left of
    the combined cut is <= everything right, with balanced halves.

    Time:  O(log(min(m, n))).  Space: O(1).
    """
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    half = (m + n + 1) // 2
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2          # cut in a
        j = half - i                # cut in b
        a_left = a[i - 1] if i > 0 else float("-inf")
        a_right = a[i] if i < m else float("inf")
        b_left = b[j - 1] if j > 0 else float("-inf")
        b_right = b[j] if j < n else float("inf")
        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2.0
        if a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1
    raise ValueError("inputs were not sorted")

from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    The k most frequent elements.

    Count frequencies, then bucket by frequency (index = count) and read buckets
    from high to low. Bucket sort gives linear time vs. O(n log n) full sort.

    Time:  O(n).  Space: O(n).
    """
    counts = Counter(nums)
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for value, freq in counts.items():
        buckets[freq].append(value)
    out: List[int] = []
    for freq in range(len(buckets) - 1, 0, -1):
        for value in buckets[freq]:
            out.append(value)
            if len(out) == k:
                return out
    return out

from typing import List


def merge_sorted(a: List[int], b: List[int]) -> List[int]:
    """
    Merge two already-sorted lists into one sorted list.

    Classic two-pointer merge (the merge step of merge sort).

    Time:  O(m + n).  Space: O(m + n) for the result.
    """
    i = j = 0
    merged: List[int] = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i]); i += 1
        else:
            merged.append(b[j]); j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

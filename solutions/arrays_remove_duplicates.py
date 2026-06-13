from typing import List


def remove_duplicates(nums: List[int]) -> List[int]:
    """
    Return the elements with duplicates removed, preserving first-seen order.

    A set tracks what's been emitted; dict.fromkeys would also work.

    Time:  O(n).  Space: O(n).
    """
    seen: set[int] = set()
    out: List[int] = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

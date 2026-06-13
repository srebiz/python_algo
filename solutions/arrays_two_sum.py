from typing import List, Optional, Tuple


def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Return indices of the two numbers adding to target, or None.

    One pass: for each value, check if its complement was already seen.

    Time:  O(n).  Space: O(n).
    """
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return seen[target - x], i
        seen[x] = i
    return None

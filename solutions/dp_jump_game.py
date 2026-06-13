from typing import List


def can_jump(nums: List[int]) -> bool:
    """
    Each value is the max jump length from that index. Return True if the last
    index is reachable from index 0.

    Greedy: track the farthest reachable index; if any index exceeds it, we're stuck.

    Time:  O(n).  Space: O(1).
    """
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + jump)
    return True

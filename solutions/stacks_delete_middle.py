from typing import List


def delete_middle(stack: List[int]) -> List[int]:
    """
    Delete the middle element of a stack using only stack operations
    (recursion provides the auxiliary storage).

    Pop down to the middle, drop it, then push the rest back.

    Time:  O(n).  Space: O(n) recursion.
    """
    def helper(s: List[int], k: int) -> None:
        if k == 0:
            s.pop()
            return
        top = s.pop()
        helper(s, k - 1)
        s.append(top)

    if stack:
        helper(stack, len(stack) // 2)
    return stack

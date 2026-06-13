from typing import List


def next_greater_elements(nums: List[int]) -> List[int]:
    """
    For each element, the next element to its right that is strictly greater,
    or -1 if none.

    Monotonic decreasing stack of indices: when a larger value arrives, it
    resolves every smaller pending index.

    Time:  O(n).  Space: O(n).
    """
    result = [-1] * len(nums)
    stack: List[int] = []                  # indices, values decreasing
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            result[stack.pop()] = x
        stack.append(i)
    return result

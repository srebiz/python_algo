from typing import List


def first_missing_positive(nums: List[int]) -> int:
    """
    Smallest positive integer absent from the array, in O(n) time / O(1) space.

    Index-as-hash: place each value v in [1, n] at position v-1 via swaps, then
    the first slot whose value != index+1 reveals the answer.

    Time:  O(n).  Space: O(1).
    """
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            target = nums[i] - 1
            nums[i], nums[target] = nums[target], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

from functools import cmp_to_key
from typing import List


def largest_number(nums: List[int]) -> str:
    """
    Arrange numbers to form the largest possible concatenated value.
    [3, 30, 34, 5, 9] -> "9534330".

    Custom comparator: a before b iff a+b > b+a as strings. Leading-zero guard
    handles all-zero input ([0, 0] -> "0").

    Time:  O(n log n * k) — k = max digit length.  Space: O(n).
    """
    strs = list(map(str, nums))

    def cmp(x: str, y: str) -> int:
        if x + y > y + x:
            return -1
        if x + y < y + x:
            return 1
        return 0

    strs.sort(key=cmp_to_key(cmp))
    result = "".join(strs)
    return "0" if result[0] == "0" else result

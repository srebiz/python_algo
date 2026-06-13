from typing import List


def max_stolen_value(houses: List[int]) -> int:
    """
    Maximum loot without robbing two adjacent houses.
    ("Find Maximum Possible Stolen Value from Houses.")

    DP rolled into two scalars: best including vs. excluding the current house.

    Time:  O(n).  Space: O(1).
    """
    prev_no, prev_yes = 0, 0       # best excluding / including previous house
    for value in houses:
        prev_no, prev_yes = max(prev_no, prev_yes), prev_no + value
    return max(prev_no, prev_yes)

from typing import List


def trap(heights: List[int]) -> int:
    """
    Total rainwater trapped between bars. Water above a bar is bounded by the
    shorter of the tallest walls to its left and right.

    Two pointers tracking running left_max / right_max; advance the side with
    the smaller max, where the trapped amount is already determined.

    Time:  O(n).  Space: O(1).
    """
    if not heights:
        return 0
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]
    total = 0
    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, heights[left])
            total += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            total += right_max - heights[right]
    return total

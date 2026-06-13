from typing import List


def max_area(heights: List[int]) -> int:
    """
    Two vertical lines + the x-axis form a container; return the most water it
    can hold. Area = min(height) * width.

    Two pointers from the ends; always move the shorter wall inward, since the
    short wall caps the area and only a taller wall could improve it.

    Time:  O(n).  Space: O(1).
    """
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        best = max(best, min(heights[left], heights[right]) * (right - left))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best

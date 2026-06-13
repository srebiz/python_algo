from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Max profit from one buy and one later sell. 0 if no profit is possible.

    Track the lowest price seen so far; the best profit is the largest
    (today's price - min so far).

    Time:  O(n).  Space: O(1).
    """
    min_price = float("inf")
    best = 0
    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)
    return best

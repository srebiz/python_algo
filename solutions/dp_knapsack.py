from typing import List


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    0/1 Knapsack: maximize total value without exceeding capacity; each item
    used at most once.

    1-D DP over capacity, iterating capacity downward so each item is counted
    once per row.

    Time:  O(n * capacity).  Space: O(capacity).
    """
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for cap in range(capacity, w - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - w] + v)
    return dp[capacity]

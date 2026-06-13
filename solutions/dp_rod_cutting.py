from typing import List


def rod_cutting(prices: List[int], length: int) -> int:
    """
    Maximum revenue from cutting a rod of `length` into pieces, where prices[i]
    is the price of a piece of length i+1.

    Unbounded-knapsack DP: dp[l] = best revenue for length l, trying every
    first-cut size.

    Time:  O(length^2).  Space: O(length).
    """
    dp = [0] * (length + 1)
    for l in range(1, length + 1):
        for cut in range(1, l + 1):
            if cut <= len(prices):
                dp[l] = max(dp[l], prices[cut - 1] + dp[l - cut])
    return dp[length]

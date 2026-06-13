from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    Fewest coins to make `amount` (unlimited supply each). -1 if impossible.

    Bottom-up DP: dp[a] = min coins for amount a; for each coin relax all
    amounts >= coin.

    Time:  O(amount * len(coins)).  Space: O(amount).
    """
    INF = amount + 1
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != INF else -1

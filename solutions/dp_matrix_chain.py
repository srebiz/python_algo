from typing import List


def matrix_chain_order(dims: List[int]) -> int:
    """
    Minimum scalar multiplications to multiply a chain of matrices, where
    matrix i has dimensions dims[i-1] x dims[i].

    Interval DP: dp[i][j] = best cost to multiply matrices i..j; try every split
    point k and combine.

    Time:  O(n^3).  Space: O(n^2).
    """
    n = len(dims) - 1
    if n < 2:
        return 0
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                dp[i][j] = min(dp[i][j], cost)
    return int(dp[1][n])

def max_product_after_cutting(n: int) -> int:
    """
    Cut a rope of length n into at least two integer pieces to maximize the
    product of piece lengths.

    DP: dp[i] = best product for length i; for each first cut j, the remainder
    can be left whole (j*(i-j)) or cut further (j*dp[i-j]).

    Time:  O(n^2).  Space: O(n).
    """
    if n <= 1:
        return 0
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
    return dp[n]

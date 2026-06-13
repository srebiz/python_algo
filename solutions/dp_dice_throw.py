def count_dice_ways(num_dice: int, faces: int, target: int) -> int:
    """
    Number of ways to roll `num_dice` dice (each 1..faces) summing to `target`.

    DP where dp[d][t] = ways to reach sum t with d dice; each die contributes a
    face value 1..faces.

    Time:  O(num_dice * target * faces).  Space: O(target).
    """
    dp = [0] * (target + 1)
    dp[0] = 1
    for _ in range(num_dice):
        nxt = [0] * (target + 1)
        for t in range(1, target + 1):
            for f in range(1, faces + 1):
                if t - f >= 0:
                    nxt[t] += dp[t - f]
        dp = nxt
    return dp[target]

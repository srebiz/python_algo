def egg_drop(eggs: int, floors: int) -> int:
    """
    Minimum number of trials needed, in the worst case, to find the critical
    floor with `eggs` eggs and `floors` floors.

    DP on "moves": dp[m][e] = highest number of floors solvable in m moves with
    e eggs = dp[m-1][e-1] (egg breaks) + dp[m-1][e] (survives) + 1. Find the
    smallest m whose reach covers all floors.

    Time:  O(eggs * floors) worst case.  Space: O(eggs).
    """
    dp = [0] * (eggs + 1)
    moves = 0
    while dp[eggs] < floors:
        moves += 1
        for e in range(eggs, 0, -1):
            dp[e] = dp[e - 1] + dp[e] + 1
    return moves

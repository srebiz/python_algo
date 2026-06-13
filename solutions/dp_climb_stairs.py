def count_ways_to_climb(n: int) -> int:
    """
    Number of distinct ways to climb n stairs taking 1 or 2 steps at a time.
    ("Count Ways to Reach the N'th Stair.")

    Ways(n) = Ways(n-1) + Ways(n-2) — a Fibonacci recurrence — rolled forward
    with two variables.

    Time:  O(n).  Space: O(1).
    """
    if n <= 2:
        return n
    prev, cur = 1, 2
    for _ in range(3, n + 1):
        prev, cur = cur, prev + cur
    return cur

from typing import List


def fibonacci_series(n: int) -> List[int]:
    """
    Return the first n Fibonacci numbers, starting 0, 1, 1, 2, ...

    Iterative rolling pair — no recursion, no memo table.

    Time:  O(n).  Space: O(1) beyond the output list.
    """
    if n <= 0:
        return []
    series = [0, 1][:n]
    a, b = 0, 1
    while len(series) < n:
        a, b = b, a + b
        series.append(b)
    return series

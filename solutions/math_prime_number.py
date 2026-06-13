def is_prime(n: int) -> bool:
    """
    Return True if n is prime.

    Trial division only up to sqrt(n), skipping evens after checking 2,
    since a composite n must have a factor <= sqrt(n).

    Time:  O(sqrt(n)).  Space: O(1).
    """
    if n < 2:
        return False
    if n < 4:
        return True            # 2 and 3
    if n % 2 == 0:
        return False
    f = 3
    while f * f <= n:
        if n % f == 0:
            return False
        f += 2
    return True

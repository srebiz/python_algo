def is_armstrong(n: int) -> bool:
    """
    Return True if n equals the sum of its own digits each raised to the power
    of the digit count (e.g. 153 = 1^3 + 5^3 + 3^3).

    Time:  O(d) — d = number of digits.  Space: O(d) for the digit string.
    """
    if n < 0:
        return False
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

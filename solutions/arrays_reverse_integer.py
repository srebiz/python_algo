def reverse_integer(x: int) -> int:
    """
    Reverse the digits of a signed 32-bit integer. Return 0 on overflow
    (result outside [-2^31, 2^31 - 1]).

    Time:  O(d) — d = number of digits.  Space: O(d) for the string step.
    """
    sign = -1 if x < 0 else 1
    rev = sign * int(str(abs(x))[::-1])
    if rev < -(2 ** 31) or rev > 2 ** 31 - 1:
        return 0
    return rev

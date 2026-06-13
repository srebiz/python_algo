def count_decodings(digits: str) -> int:
    """
    Number of ways to decode a digit string where 'A'..'Z' map to "1".."26".

    DP: ways[i] depends on the single digit at i-1 (if 1..9) and the two-digit
    pair ending at i (if 10..26). Rolled into two variables.

    Time:  O(n).  Space: O(1).
    """
    if not digits or digits[0] == "0":
        return 0
    prev2, prev1 = 1, 1            # ways up to i-2, i-1
    for i in range(1, len(digits)):
        cur = 0
        if digits[i] != "0":
            cur += prev1
        if 10 <= int(digits[i - 1:i + 1]) <= 26:
            cur += prev2
        if cur == 0:
            return 0              # invalid like "30"
        prev2, prev1 = prev1, cur
    return prev1

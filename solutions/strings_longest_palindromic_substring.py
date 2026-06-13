def longest_palindromic_substring(s: str) -> str:
    """
    Return a longest substring of s that is a palindrome.

    Expand-around-center: every palindrome has a center (a char for odd
    lengths, a gap for even). Try all 2n-1 centers, expanding outward.

    Time:  O(n^2).  Space: O(1).
    """
    if not s:
        return ""

    def expand(left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1            # last valid bounds

    start, end = 0, 0
    for i in range(len(s)):
        l1, r1 = expand(i, i)                  # odd-length center
        l2, r2 = expand(i, i + 1)              # even-length center
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2
    return s[start:end + 1]
